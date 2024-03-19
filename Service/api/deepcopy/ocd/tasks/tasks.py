import pandas as pd

import Service.mysql.db as db
import time

from Service.api.deepcopy.ocd import quey_interface
from Service.api.deepcopy.ocd.utility import check_web_article_exists, make_merge_return_object, \
    merge_rows_into_table_based_on, check_article_exists, MERGE_KEYS, MERGE_KEYS_BULK_MODE
from Service.api.export_program.table_links import OCD_LINKS
from Service.api.export_program.util import update_table_links, HashMaker


def merge_article_with_deepcopy(*, article: str, program: str, merge_with: str) -> dict[str, str | int]:

    start = time.perf_counter()
    web_program_name = merge_with
    print(f"args :: article={article} ; program={program} ; merge_with={web_program_name}")
    assert article and program and web_program_name, "article, program, merge_with need to be specified."
    article = article.strip()
    program = program.strip()
    web_program_name = web_program_name.strip()
    """ check if article already exists in program and return """
    exists = check_web_article_exists(article=article, program=program, web_program_name=web_program_name)
    if exists:
        print(f"{article} {program} already exists in {web_program_name}")
        return make_merge_return_object(
            message=f"'{article}' von '{program}' bereits in {web_program_name} enthalten.",
            time_start=start,
            status=0
        )

    """ check if article exists at all """
    exists = check_article_exists(article=article, program=program)
    if not exists:
        print(f"{article} {program} doesnt exist.")
        return make_merge_return_object(
            message=f"'{article}' nicht in '{program}' gefunden.",
            time_start=start,
            status=0
        )

    article_numbers_and_programs = [(article, program, )]
    insertion_count_all = 0
    with db.new_connection() as read_connection:
        with read_connection.cursor(dictionary=True) as c:
            tables_2_yield = quey_interface.deepcopy_query(article_numbers_and_programs, c)
            with db.new_connection() as write_connection:
                for table_name, result_set in tables_2_yield:
                    """ article has no data in this table """
                    if len(result_set) == 0:
                        continue
                    """ make df of result set for easier editing """
                    df = pd.DataFrame(result_set)
                    """ remove/replace columns for new article data """
                    df = df.drop("db_key", axis=1)
                    df["web_filter"] = 0
                    df["web_program_name"] = merge_with

                    print("table_name::", table_name, len(result_set))
                    merge_keys = MERGE_KEYS_BULK_MODE[table_name]
                    grouped = df.groupby(merge_keys)
                    # print("grouped rel dfs", grouped.size)
                    for _, group_df in grouped:
                        print("GROUP....", group_df.size)
                        # print(type(_), type(group_df), group_df.size)
                        # print(group_df.to_string())
                        # input(".")

                        result_set = group_df.to_dict('records')
                        insertion_count = merge_rows_into_table_based_on(
                            merge_keys,
                            result_set,
                            f"web_{table_name}",
                            merge_with,
                            write_connection,
                            bulk_mode=True
                        )
                        insertion_count_all += insertion_count
                        print("::::insertion_count", f"web_{table_name}", insertion_count)

                    # merge_rows_into_table_based_on(
                    #     MERGE_KEYS[table_name],
                    #     result_set,
                    #     f"web_{table_name}",
                    #     web_program_name,
                    #     write_connection
                    # )
                write_connection.commit()

    print("insertion_count_all", insertion_count_all)
    return make_merge_return_object(
        message=f"'{article}' von '{program}' mit '{web_program_name}' gemerged",
        time_start=start,
        status=1
    )


def merge_article_with_deepcopy_as(article, program, merge_as, merge_with):
    """ merges article as own separate thing where keys will be unique to this article """
    start = time.perf_counter()
    """ check if article already exists in program and return """
    exists = check_web_article_exists(article=merge_as, program=program, web_program_name=merge_with)
    if exists:
        print(f"{merge_as} {program} already exists in {merge_with}")
        return make_merge_return_object(
            message=f"'{merge_as}' von '{program}' bereits in {merge_with} enthalten.",
            time_start=start,
            status=0
        )
    """ check if article exists at all """
    exists = check_article_exists(article=article, program=program)
    if not exists:
        print(f"{article} {program} doesnt exist.")
        return make_merge_return_object(
            message=f"'{article}' nicht in '{program}' gefunden.",
            time_start=start,
            status=0
        )
    ocd_links = OCD_LINKS
    article_numbers_and_programs = [(article, program,)]
    insertion_count_all = 0
    with db.new_connection() as read_connection:
        with read_connection.cursor(dictionary=True) as c:
            tables_2_yield = quey_interface.deepcopy_query(article_numbers_and_programs, c)
            with db.new_connection() as write_connection:
                hash_maker = HashMaker()
                for table_name, result_set in tables_2_yield:
                    """ article has no data in this table """
                    if len(result_set) == 0:
                        continue
                    """ make df of result set for easier editing """
                    df = pd.DataFrame(result_set)
                    """ make columns, that link somewhere, unique """
                    if table_name in ocd_links:
                        update_table_links(table=df,
                                           linking_columns=ocd_links[table_name],
                                           hash_maker=hash_maker,
                                           unify_by="VALUE",  # TODO: not so good idea to make EVERYTHING unique
                                           unify_string=merge_as)
                    """ set the new article_nr in tables where article_nr is stored """
                    if table_name in ["ocd_article", "ocd_artbase", "ocd_packaging", "ocd_articletaxes", "ocd_price", "ocd_propertyclass"]:
                        df["article_nr"] = merge_as

                    """ remove/replace columns for new article data """
                    df = df.drop("db_key", axis=1)
                    df["web_filter"] = 0
                    df["web_program_name"] = merge_with

                    # print("SKIP ocd_relation......", df.size)
                    merge_keys = MERGE_KEYS_BULK_MODE[table_name]
                    grouped = df.groupby(merge_keys)
                    # print("grouped rel dfs", grouped.size)
                    for _, group_df in grouped:
                        print("GROUP....", group_df.size)
                        # print(type(_), type(group_df), group_df.size)
                        # print(group_df.to_string())
                        # input(".")

                        result_set = group_df.to_dict('records')
                        insertion_count = merge_rows_into_table_based_on(
                            merge_keys,
                            result_set,
                            f"web_{table_name}",
                            merge_with,
                            write_connection,
                            bulk_mode=True
                        )
                        insertion_count_all += insertion_count
                        print("::::insertion_count", f"web_{table_name}", insertion_count)
                    # else:
                    #     result_set = df.to_dict('records')
                    #     merge_rows_into_table_based_on(
                    #         MERGE_KEYS[table_name],
                    #         result_set,
                    #         f"web_{table_name}",
                    #         merge_with,
                    #         write_connection
                    #     )
                write_connection.commit()
    print("insertion_count_all", insertion_count_all)
    return make_merge_return_object(
        message=f"'{article}' von '{program}' als '{merge_as}' gemerged",
        time_start=start,
        status=1
    )

