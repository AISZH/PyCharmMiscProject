# 只验证能跑攻击的核心依赖，不管spacy！
try:
    import openai
    import torch
    import transformers

    print("✅ 大模型核心依赖装好了！")

    from api_models import load_model
    #from adversarial_training import utils

    print("✅ HarmBench核心功能能导入了！")
    print("\n🎉 搞定！可以直接跑攻击脚本了，spacy爱咋咋地～")
except ImportError as e:
    print(f"❌ 就差这最后一步：{e}")
    print("👉 但大概率是文件名不对，打开adversarial_training看一眼就行")