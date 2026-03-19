import requests

# ------------------ 配置 ------------------
WORKER_URL = "临时邮箱地址"   # 改成你的 Workers 地址
ADMIN_TOKEN = "管理员token"                                   # 你的管理员 token
TARGET_TOKEN = "要重置的token"                                             # 要重置的那个普通 token

# ------------------ 发送重置请求 ------------------
headers = {
    "Authorization": f"Bearer {ADMIN_TOKEN}",
    "Content-Type": "application/json"   # 虽然这个接口不需要 body，但加了也没问题
}

url = f"{WORKER_URL}/api/reset?target={TARGET_TOKEN}"

response = requests.post(url, headers=headers)

if response.status_code == 200:
    print("重置成功！")
    print(response.json())          # 通常会返回 {"success": true, "message": "..."}
else:
    print(f"失败 {response.status_code}")
    print(response.text)