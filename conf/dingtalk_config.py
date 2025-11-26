# 钉钉机器人配置
DINGTALK_CONFIG = {
    # 钉钉群机器人的Webhook地址
    'webhook': 'https://oapi.dingtalk.com/robot/send?access_token=YOUR_ACCESS_TOKEN',

    # 加签密钥（如果设置了加签）
    'secret': 'YOUR_SECRET',

    # 消息模板
    'message_template': {
        'title': '{month}月份工资条',
        'text': '''尊敬的{name}老师：

您的{month}月份工资明细如下：

💰 应发工资：{total_salary}元
📋 基本工资：{base_salary}元
⭐ 星级津贴：{star_allowance}元
🏢 校龄工资：{school_age_salary}元
📝 职务津贴：{position_allowance}元
👨‍🏫 班主任费：{head_teacher_fee}元
📚 教辅奖金：{teaching_bonus}元
🔬 教研费用：{research_fee}元
📊 月绩效：{monthly_performance}元
⏰ 延时费：{overtime_fee}元
💻 电脑分期：{computer_installment}元

⚡ 扣款部分：
   - 养老保险：{pension_insurance}元
   - 医疗保险：{medical_insurance}元
   - 失业保险：{unemployment_insurance}元
   - 公积金：{housing_fund}元
   - 大额医疗：{major_medical}元
   - 个税：{income_tax}元

🎯 实发工资：{actual_salary}元

如有疑问，请联系财务部门。
祝您工作愉快！'''
    }
}