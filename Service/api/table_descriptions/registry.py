import datetime


def make_registry(program: str, program_id: str, depend_programs: list[str]) -> str:

    depend = ";".join([
        "::ofml::oi::1.29.0/ANY",
        "::kn::basics::2.21.0/DE",
        *[f"::kn::{_}::2.21.0/DE" for _ in depend_programs]
    ])

    timestamp = datetime.datetime.now()

    return __make_registry(
        program=program,
        program_name=program.upper(),
        program_id=program_id,
        release_date=timestamp.strftime("%Y-%m-%d"),
        release_timestamp=timestamp.strftime("%Y%m%d%H%M%S"),
        depend=depend

)


def __make_registry(**kwargs):
    global __REGISTRY
    return __REGISTRY.format(**kwargs)


__REGISTRY = """
#--------------------------
# manufacturer information
manufacturer=kn
manufacturer_id=KN
manufacturer_name=König + Neurath AG

#--------------------------
# package information
program={program}
program_name={program_name}
program_id={program_id}

#--------------------------
# catalog information
type=product
category=furniture
languages=de
distribution_region=DE
version=2
release_version=2.21.0
release_date={release_date}
release_timestamp={release_timestamp}
cat_type=XCF

#--------------------------
# product-database
pd_format=OCD_4.1
productdb=::kn::basics::KnNativeOCDProductDB41
productdb_path=kn/{program}/DE/2/db
oam_path=kn/{program}/DE/2/oam

#--------------------------
# program-database
proginfo=::kn::basics::KnProgInfo
proginfodb_path=kn/basics/2

#--------------------------
# relations and dependencies
depend={depend}

#--------------------------
# additional settings
series_type=go_meta
meta_type=::ofml::go::GoMetaType;::ofml::go::goGetMetaType();::ofml::go::goSetup([[@FIRST, @{program}]])
geo_export_params=use_proxy_geometries
persistency_form=STATECODES
insertion_mode=APP_DEFAULT

[de]
manufacturer_name=König + Neurath AG
program_name={program_name}
description=König + Neurath - {program_name}
copyright=1998-2023 by König + Neurath

"""

# import pandas as pd
#
# df = pd.DataFrame(
#     columns=["C1", "C2"],
#     data=[
#     ["A11", "A12"],
#     ["B11", "B12"],
#     ["C11", "C12"],
#     ["D11", "D12"],
#     ["E11", "E12"],
#     ["F11", "F12"],
#     ["G11", "G12"],
#     ])
# #
# print(df.to_string())
# print("##############")
# print("##############")
# print("##############")

#
# df[["C1", "C2"]] = df[["C1", "C2"]] + "--X"
#
# #df[["C1", "C2"]] = df[["C1", "C2"]] + df["C1"].tolist()
#
# df["C1"] = df["C1"] + df["C1"].tolist()
#
# #df["3"] = ["X1", "X2", "X3", "X4", "X5", "X6", ]
#
# print(df.to_string())

#
# def f(x: pd.Series):
#     print(f"f({type(x)}", x.index, x.name)
#     print(x.to_string())
#     if x.name == "C2":
#         return x.apply(lambda a : a + "----")
#     else:
#         return x
#
#
# df = df.apply(f)
#
#
# print(df.to_string())