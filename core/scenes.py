academic_scenes = [
    '建筑',
    '工业设计/艺术',
    '城市规划',
    '手工艺品（编织、针织、织物、家具、雕刻、马赛克、陶瓷、民间艺术）',
    '洞穴/岩画',
    '音乐和音乐史',
    '摄影',
    '戏剧历史',
    '戏剧',
    '环境科学',
    '文学和作家',
    '书籍、报纸、杂志、期刊',
    '动植物灭绝或保护行动',
    '鱼类和其他水生生物',
    '细菌和其他微生物',
    '医学技术',
    '公共卫生',
    '感官器官的生理学',
    '生物化学',
    '动物行为（迁徙、觅食、防御）',
    '栖息地及其对动植物的适应性',
    '营养及其对身体的影响',
    '动物交流',
    '天气和大气',
    '海洋学',
    '冰川、冰川地形、冰河时期',
    '沙漠和其他极端环境',
    '污染、替代能源、环境政策',
    '其他行星的大气',
    '天文学',
    '宇宙学',
    '光学性质、光学',
    '声学特性',
    '电磁辐射',
    '粒子物理学',
    '电视、广播、雷达技术',
    '无机物质的化学',
    '计算机科学',
    '地震学（板块结构、地震、构造）',
    '心理学',
    '经济学',
    '社会科学',
    '社会心理学',
    '政治学',
    '教育学',
    '人类学',
    '艺术历史',
    '语言学',
    '海洋生物学',
    
]

school_scenes = {
    "学校食堂场景": ['饭菜口味', '食堂优惠政策', '卫生安全', '食堂政策'],
    "学校宿舍场景": ['宿舍安排', '学生校外租房', '房间设施问题', '室友相处问题', '宿舍政策/管理制度'],
    "学校图书馆场景": ['借阅书籍', '还书问题', '图书馆复习准备', '论文准备', '图书馆设施', '查询资料', '借还书流程', '购买书籍', '美国大学图书馆制度', '借还书问题'],
    "学校假期场景": ['假期旅行', '回忆假期活动', '推荐的假期活动'],
    "在学校办公室跟教授": ['课程请假', '延期交作业', '论文准备', '选课咨询', '论文选题', '论文写作', '论文问题','课程进度跟不上'],
    "学生注册场景": ['开学注册问题', '缴费问题', '毕业需求', '课程学分计算', '报到注册时间', '报到注册准备材料', '报到注册问题'],
    "学术选课场景": ['选课问题', '选课困难', '选课过多', '退课和放弃课程', '学生情况分析'],
    "学校维护场景": ['教室设施损坏', '宿舍物品损坏', '维护时间协商'],
    "学生就业场景": ['兼职工作', '协调工作与课程时间', '招聘应聘', '参加招聘会', '工作条件与工资', '工作待遇和时间', '职业咨询'],
    "学校奖学金场景": ['奖学金申请', '奖学金问题', '奖学金种类咨询', '奖学金资格', '奖学金申请材料', '申请奖学金可能性'],
    "学校社团场景": ['场地申请', '社团申请', '社团招生', '社团活动', '社团问题', '社团设立与改动', '社团场所'],
    "学校课程场景": ['课堂问题讨论', '教学质量评价', '课堂作业', '考试安排', '调课事宜', '课程辅助材料', '考试复习', '课程介绍', '作业类型与提交方式', '论文分数', '请教课堂内容',
               '迟到或旷课理由'],
    "学生转学场景": ['转学或转专业理由', '特殊转学情况', '转学申请流程'],
    "学生组织活动场景": ['常参加和组织的活动', '活动目的', '活动内容'],
    "学校医院场景": ["保健咨询", '疫苗接种', '保险要求、自费项目和费用报销流程', '看病就诊', '医疗预约', '就诊流程'],
    "学生社交场景": ['社交活动', '社交困扰和人际关系', '交友、社交焦虑和群体活动'],
    "校园安全场景": ['校园警报', '失物招领', '紧急救援'],
    "校园交通场景": ['校车服务', '自行车道', '停车许可', '交通规则'],
    "学校体育场馆场景": ['场馆预约', '体育课选项', '健身设施开放时间'],
    "校园生活服务场景": ['邮件投递', '银行服务', '学生证办理'],
    "学生投诉与反馈场景": ['学生反馈渠道', '解决投诉流程和改善措施', '学生投诉和反馈问题'],
    "学生毕业场景":['沟通毕业要求','提交毕业申请']
}

scene = {
    "词汇题": '按照新托福阅读词汇题模式，对{}单词生成英语阅读短文、英文问题（{}在短文中跟以下选项那个意思相近？）、生成四个英文选项，不需要生成选项答案。',
    "词汇阅读": "用这些单词({})生成一篇阅读理解文章",
    "英语对话": "Let's talk about {}.",
    "随机话题": "Can you give a randomly topic to me.",
    "讲座": "新托福听力阅读为模板。以{}为主题，生成一篇大学教授给学生讲课的文章。文章中会涉及到具体的例子，以及教授会对例子进行具体说明。英文输出内容。",
    "讲座对话": "新托福听力阅读为模板。以{}为主题，生成一篇大学教授给学生讲课的文章。文章中会涉及到具体的例子，以及教授会对例子进行具体说明。内容用英文输出。教授和一个学生对话分别用P1:和P2:表示。对话内容不少于30段。",
    "单词分析": "对{}单词进行详细分析，包括词根词缀、单词含义以及对应的使用例子。",
    "扮演角色": "我想让你扮演我的{}，根据你的角色职责使用英语向我提问一个问题。如果你不确定具体角色设定，可以参考现实生活生成角色背景。",
    "阅读题目": "根据新托福阅读理解文章的选择题类型，生成五道选择题，不需要生成答案。",
    "阅读答案": "根据上面选择题，生成答案和解释。",
    "学校": "根据新托福听力模板，生成{}的英语对话，内容包括{}等话题，两人讨论话题会延申到其他{}话题上面。两人对话分别用P1:和P2:表示。对话内容不少于30段。英文输出内容。",
    "语法批改": "Help me check if there are any English grammar errors in these contents: {}",
    "托福独立口语task1批改":"根据新托福口语TASK1的评分标准，对以下回答进行评分和中文解释说明为什么这么评分。并且使用中文说明有什么不足和优化空间。\n题目是：{}\n我的回答：{}",
    "托福独立口语task1答案生成":"以新托福独立口语标准，英语回答以下问题，选择一个观点回答，回答的单词不多于120个词语。其中回答不使用复杂的词汇。{}\n",
    "托福独立口语task2意见生成":'针对于上面这个话题，两位学生分别表达了自己的观点（同意或者反对）和使用对应的例子进行说明。两人对话分别用P1:和P2:表示。对话内容不少于20段。英文输出内容。',

}

toefl_scenes = {
    "oral_task2": [
        '根据新托福口语题目中TASK2类型，生成大学将要实施某个政策并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
        '根据新托福口语题目中TASK2类型，生成大学将要实施某个程序并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
        '根据新托福口语题目中TASK2类型，生成大学将要实施某个规则并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
        '根据新托福口语题目中TASK2类型，生成大学将要实施某个计划并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
        '根据新托福口语题目中TASK2类型，生成大学将要对校园设施做某事并且产生什么效果的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
        '根据新托福口语题目中TASK2类型，生成大学做某事会提升或者降低校园生活质量的英语阅读材料。参考现实生活的大学公告或者电子邮件或者信件。单词数在80到110个单词之间。',
    ],

}
