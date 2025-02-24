import re
import asyncio
from aiohttp import TCPConnector, ClientSession
import pyecharts.options as opts
from pyecharts.charts import TreeMap

async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()

# 获取官方的数据
data = asyncio.run(
    get_json_data(
        url="https://echarts.apache.org/examples/data/asset/data/ec-option-doc-statistics-201604.json"
    )
)
tree_map_data: dict = {"children": []}

def convert(source, target, base_path: str):
    for key in source:
        if base_path != "":
            path = base_path + "." + key
        else:
            path = key
        if re.match(r"/^\$/", key):
            pass
        else:
            child = {"name": path, "children": []}
            target["children"].append(child)
            if isinstance(source[key], dict):
                convert(source[key], child, path)
            else:
                target["value"] = source["$count"]

convert(source=data, target=tree_map_data, base_path="")
(
    TreeMap(init_opts=opts.InitOpts(width="1900px", height="720px"))
    .add(
        series_name="option",
        data=tree_map_data["children"],
        visual_min=300,
        leaf_depth=1,
        # 标签居中为 position = "inside"
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(
            title="Echarts 配置项查询分布", subtitle="2020/9", pos_left="leafDepth"
        ),
    )
    .render("../source_material/02/07-矩形树图.html")
)
