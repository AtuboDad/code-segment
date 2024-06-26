import zhipuai
from zhipuai import ZhipuAI


# zhipuai.api_key = "your api key"
client = ZhipuAI(api_key="your api key")

response = client.chat.completions.create(
    model="glm-4",
    prompt= [{"role":"user","content":"从文档\n\"\"\"\n建设项目规模：新建一座地下2层地上17层的商业办公综合楼，并配套建设地下停车场等设施，总用地面积4246.3平方米，总建筑面积21175.56平方米。\n\n建设项目规模：本工程位于青阳街道鼓声路1号，总建筑面积为2722.44m2，占地面积723.84m2，地上4层，建筑总高度13.75m，A~E轴部分为砖混结构，F~H部分为框架结构，主要建设内容为基础扩大加固、对柱梁板进行碳纤维布及植筋加固，并对楼地面和天棚及门窗等修缮。项目总投资概算916万元。\n\n建设项目规模：总用地面积约22334平方米，总建筑面积约81296平方米。地上面积约62535平方米，地下面积约18761平方米。项目主要建设内容包括但不限于：住宅建筑、社区服务配套用房以及道路、广场、停车场、给排水管网、供配电设备、绿化工程等。\n\n建设项目规模：全长约6.86公里，其中石永路~石永二路段长约3.73公里，道路等级为二级公路兼城市主干路，道路红线宽度为33.5~53米，主路采用双向四车道~双向六车道，设计时速为60km/h;石永二路~石锦路段长约3.13公里,道路等级为一级公路兼城市主干路，道路红线宽度为90米，主路采用双向八车道，设计时速为60km/h，建设内容:包括道路工程、交通工程、桥涵工程、管线综合、照明及绿化工程等。\n\n建设项目规模：该项目采取以工代赈 模式，拟新建4.525公里水泥混凝土道路，宽6.5米，采用全幅式路面，包括道路路基、道路路面、交通设施等建设。\n\n建设项目规模：G355线K295+410~K300+000段路面沥青罩面工程，起点位于安溪县虎邱镇双都村，起点桩号K295+410，途经虎邱镇双都村、罗岩村，设计终点 K300+000,路线里程4.59公里，现状道路为四级公路、设计速度20km/h、双向两车道。\n\n建设项目规模：S312线K141+240-K141+390段灾毁重建工程位于安溪县尚卿乡，测设起点桩号K141+240，测设终点桩号K141+390，路线长度0.15公里。\n\n建设项目规模：本次林辋溪里段安全生态水系建设项目设计范围为林辋溪干流的溪边水闸至团结桥之间河段约4.59km，松星溪支流约1.0km，灵山支流0.1km，村下村支流约0.66km，总长度约6.35km。主要建设内容包括河道清淤、护岸改造提升、河岸绿化、亲水景观节点、发电机房等。\n\n建设项目规模：水库正常蓄水位605m，设计洪水位606.49m，校核洪水位606.82m，死水位588.0m，最大坝高38m，总库容63.5万m3，兴利库容48.1万m3，库容系数11.0%，为不完全年调节水库。需水量预测成果，同意水库兴利调度原则以及兴利调节计算结论。工程建成后，北苏板水库与曲斗水库联合8014.86调节 95%供水保证率多年平均可供水量为126.4万m3，90%保证 率多年平均灌溉水量为10万m3。\n\n建设项目规模：水库正常蓄水位733m，总库容78.84万m3，正常蓄水位以下库容61.07万m3，兴利库容51.20万m3，库容系数6.27%，为 月调节水库。水库涉及下泄生态流量0.026m3/s，需水预测采用的定额及农业、生活等需水量成 果，水资源供需平衡分析结论。工程建成后，设计供水 保证率95%，供水水量为111.69万m3，设计灌溉保证率90%，灌溉水量为9.3万m3。\n\n\"\"\"\n中找问题\n\"\"\"\nG355线路里程\n\"\"\"\n的答案，找到答案就仅使用文档语句回答问题，找不到答案就用自身知识回答并且告诉用户该信息不是来自文档。\n\n不要复述问题，直接开始回答。"}],
    temperature= 0.7,
    top_p= 0.7,
    incremental=False,
)



for event in response.events():
    if event.event == "add":
        print(event.data)
    elif event.event == "error" or event.event == "interrupted":
        print(event.data)
    elif event.event == "finish":
        print(event.data)
        print(event.meta)
    else:
        print(event.data)