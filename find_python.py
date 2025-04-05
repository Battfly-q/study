import subprocess
import os
import sys

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except Exception as e:
        return None

def find_python_paths():
    print("正在查找已安装的 Python ...\n")

    python_version = run_command("python --version") or run_command("py --version")
    if python_version:
        print(f"✅ 检测到 Python 版本：{python_version}\n")
    else:
        print("⚠️ 未能通过命令检测到 Python 版本。\n")

    python_paths = run_command("where python")
    if python_paths:
        print("📂 Python 可执行文件路径：")
        print(python_paths)
        print("\n👉 你可以把以下路径添加到系统环境变量（PATH）中：")

        for path in python_paths.splitlines():
            base_path = os.path.dirname(path)
            print(f"- {base_path}")
            scripts_path = os.path.join(base_path, 'Scripts')
            if os.path.exists(scripts_path):
                print(f"- {scripts_path}")
        print("\n⚙️ 添加完后请重新启动命令行窗口。")
    else:
        print("❌ 没有找到 Python 安装路径（可能未安装或未添加到 PATH）")

if __name__ == "__main__":
    find_python_paths()

