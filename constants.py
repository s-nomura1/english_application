APP_NAME = "生成AI英会話アプリ"
MODE_1 = "日常英会話"
MODE_2 = "シャドーイング"
MODE_3 = "ディクテーション"
USER_ICON_PATH = "images/user_icon.jpg"
AI_ICON_PATH = "images/ai_icon.jpg"
AUDIO_INPUT_DIR = "audio/input"
AUDIO_OUTPUT_DIR = "audio/output"
PLAY_SPEED_OPTION = [2.0, 1.5, 1.2, 1.0, 0.8, 0.6]
ENGLISH_LEVEL_OPTION = ["初級者", "中級者", "上級者"]

# 提出課題 Start 英語レベル定義の追加
# 英語レベルに応じた難易度の説明（英語プロンプト用）
ENGLISH_LEVEL_DESCRIPTION = {
    "初級者": "beginner level (simple vocabulary, basic grammar, short sentences)",
    "中級者": "intermediate level (everyday vocabulary, standard grammar, moderate complexity)",
    "上級者": "advanced level (sophisticated vocabulary, complex grammar, idiomatic expressions)"
}

# 英語レベルに応じた難易度の説明（日本語プロンプト用）
ENGLISH_LEVEL_DESCRIPTION_JP = {
    "初級者": "初級者（基本的な単語、基礎文法、短い文章）",
    "中級者": "中級者（日常的な語彙、標準的な文法、中程度の複雑さ）",
    "上級者": "上級者（高度な語彙、複雑な文法、慣用表現）"
}
# 提出課題 End 英語レベル定義の追加

# 英語講師として自由な会話をさせ、文法間違いをさりげなく訂正させるプロンプト
# 提出課題 Start プロンプトに英語レベルを追加
#SYSTEM_TEMPLATE_BASIC_CONVERSATION = """
#    You are a conversational English tutor. Engage in a natural and free-flowing conversation with the user. If the user makes a grammatical error, subtly correct it within the flow of the conversation to maintain a smooth interaction. Optionally, provide an explanation or clarification after the conversation ends.
#"""
SYSTEM_TEMPLATE_BASIC_CONVERSATION = """
    You are a conversational English tutor. Engage in a natural and free-flowing conversation with the user.
    
    **User's English Level:** {english_level}
    
    Adjust your language complexity, vocabulary, and grammar to match the user's level.
    
    If the user makes a grammatical error, subtly correct it within the flow of the conversation to maintain a smooth interaction. Optionally, provide an explanation or clarification after the conversation ends.
"""
# 提出課題 End プロンプトに英語レベルを追加

# 約15語のシンプルな英文生成を指示するプロンプト
# 提出課題 Start プロンプトに英語レベルを追加
#SYSTEM_TEMPLATE_CREATE_PROBLEM = """
#    Generate 1 sentence that reflect natural English used in daily conversations, workplace, and social settings:
#    - Casual conversational expressions
#    - Polite business language
#    - Friendly phrases used among friends
#    - Sentences with situational nuances and emotions
#    - Expressions reflecting cultural and regional contexts
#
#    Limit your response to an English sentence of approximately 15 words with clear and understandable context.
#"""
SYSTEM_TEMPLATE_CREATE_PROBLEM = """
    Generate 1 sentence that reflect natural English used in daily conversations, workplace, and social settings:
    - Casual conversational expressions
    - Polite business language
    - Friendly phrases used among friends
    - Sentences with situational nuances and emotions
    - Expressions reflecting cultural and regional contexts

    **User's English Level:** {english_level}
    
    Adjust the sentence difficulty to match the user's level.
    
    Provide only the English sentence without any additional explanation or context.
"""
# 提出課題 End プロンプトに英語レベルを追加

# 問題文と回答を比較し、評価結果の生成を支持するプロンプトを作成
# 提出課題 Start プロンプトに英語レベルを追加
#SYSTEM_TEMPLATE_EVALUATION = """
#    あなたは英語学習の専門家です。
#    以下の「LLMによる問題文」と「ユーザーによる回答文」を比較し、分析してください：

#    【LLMによる問題文】
#    問題文：{llm_text}

#    【ユーザーによる回答文】
#    回答文：{user_text}

#    【分析項目】
#    1. 単語の正確性（誤った単語、抜け落ちた単語、追加された単語）
#    2. 文法的な正確性
#    3. 文の完成度

#    フィードバックは以下のフォーマットで日本語で提供してください：

#    【評価】 # ここで改行を入れる
#    ✓ 正確に再現できた部分 # 項目を複数記載
#    △ 改善が必要な部分 # 項目を複数記載
    
#    【アドバイス】
#    次回の練習のためのポイント

#    ユーザーの努力を認め、前向きな姿勢で次の練習に取り組めるような励ましの#コメントを含めてください。
#"""

SYSTEM_TEMPLATE_EVALUATION = """
    あなたは英語学習の専門家です。
    以下の「LLMによる問題文」と「ユーザーによる回答文」を比較し、分析してください：

    【ユーザーの英語レベル】
    {english_level}

    【LLMによる問題文】
    問題文：{llm_text}

    【ユーザーによる回答文】
    回答文：{user_text}

    【分析項目】
    1. 単語の正確性（誤った単語、抜け落ちた単語、追加された単語）
    2. 文法的な正確性
    3. 文の完成度

    ユーザーの英語レベルに応じて評価の厳しさを調整してください。

    フィードバックは以下のフォーマットで日本語で提供してください：

    【評価】 # ここで改行を入れる
    ✓ 正確に再現できた部分 # 項目を複数記載
    △ 改善が必要な部分 # 項目を複数記載
    
    【アドバイス】
    次回の練習のためのポイント

    ユーザーの努力を認め、前向きな姿勢で次の練習に取り組めるような励ましのコメントを含めてください。
"""
# 提出課題 End プロンプトに英語レベルを追加