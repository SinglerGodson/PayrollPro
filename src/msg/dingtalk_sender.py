import requests
import json
import hmac
import hashlib
import base64
import time
import logging
from typing import Dict, Optional, List
from urllib.parse import quote_plus
from conf.dingtalk_config import DINGTALK_CONFIG
logger = logging.getLogger(__name__)


class DingTalkSender:
    """钉钉消息发送器"""

    def __init__(self, webhook: str, secret: str = None):
        self.webhook = webhook
        self.secret = secret

    def _generate_signature(self) -> Dict:
        """生成签名（如果启用了加签）"""
        if not self.secret:
            return {}

        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = f'{timestamp}\n{self.secret}'
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = quote_plus(base64.b64encode(hmac_code))

        return {
            'timestamp': timestamp,
            'sign': sign
        }

    def send_text_message(self, content: str, at_mobiles: List[str] = None, at_all: bool = False) -> bool:
        """发送文本消息"""
        try:
            # 构建消息体
            message = {
                "msgtype": "text",
                "text": {
                    "content": content
                },
                "at": {
                    "atMobiles": at_mobiles or [],
                    "isAtAll": at_all
                }
            }

            return self._send_message(message)

        except Exception as e:
            logger.error(f"发送文本消息失败: {e}")
            return False

    def send_markdown_message(self, title: str, text: str, at_mobiles: List[str] = None, at_all: bool = False) -> bool:
        """发送Markdown格式消息"""
        try:
            message = {
                "msgtype": "markdown",
                "markdown": {
                    "title": title,
                    "text": text
                },
                "at": {
                    "atMobiles": at_mobiles or [],
                    "isAtAll": at_all
                }
            }

            return self._send_message(message)

        except Exception as e:
            logger.error(f"发送Markdown消息失败: {e}")
            return False

    def _send_message(self, message: Dict) -> bool:
        """发送消息到钉钉"""
        try:
            # 添加签名参数
            params = self._generate_signature()

            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(
                self.webhook,
                data=json.dumps(message),
                headers=headers,
                params=params,
                timeout=10
            )

            result = response.json()

            if result.get('errcode') == 0:
                logger.info("消息发送成功")
                return True
            else:
                logger.error(f"消息发送失败: {result.get('errmsg')}")
                return False

        except requests.exceptions.RequestException as e:
            logger.error(f"网络请求失败: {e}")
            return False
        except Exception as e:
            logger.error(f"发送消息时发生未知错误: {e}")
            return False

    def send_salary_notification(self, employee_data: Dict, month: str = "10") -> bool:
        """发送工资条通知"""
        try:
            # 使用配置的模板


            template = DINGTALK_CONFIG['message_template']
            title = template['title'].format(month=month)
            text = template['text'].format(
                name=employee_data['name'],
                month=month,
                total_salary=employee_data.get('total_salary', 0),
                base_salary=employee_data.get('base_salary', 0),
                star_allowance=employee_data.get('star_allowance', 0),
                school_age_salary=employee_data.get('school_age_salary', 0),
                position_allowance=employee_data.get('position_allowance', 0),
                head_teacher_fee=employee_data.get('head_teacher_fee', 0),
                teaching_bonus=employee_data.get('teaching_bonus', 0),
                research_fee=employee_data.get('research_fee', 0),
                monthly_performance=employee_data.get('monthly_performance', 0),
                overtime_fee=employee_data.get('overtime_fee', 0),
                computer_installment=employee_data.get('computer_installment', 0),
                pension_insurance=employee_data.get('pension_insurance', 0),
                medical_insurance=employee_data.get('medical_insurance', 0),
                unemployment_insurance=employee_data.get('unemployment_insurance', 0),
                housing_fund=employee_data.get('housing_fund', 0),
                major_medical=employee_data.get('major_medical', 0),
                income_tax=employee_data.get('income_tax', 0),
                actual_salary=employee_data.get('actual_salary', 0)
            )

            return self.send_markdown_message(title, text)

        except Exception as e:
            logger.error(f"发送工资通知失败: {e}")
            return False