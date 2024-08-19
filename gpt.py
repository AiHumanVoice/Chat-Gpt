import openai

# OpenAI API 키 설정
openai.api_key = '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'
# input your OpenAI API키
def ask_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # 사용할 모델 지정
        messages=[
            {"role": "system", "content": "너는 한국에 사는 굉장히 친절한 남자친구야. 구어체로 대화형식으로 해줘"},
            {"role": "user", "content": prompt + " 구어체로 숫자나 제목 없이 자연스럽게 설명해줘."},
        ],
        max_tokens=300,  # 응답에서 생성할 최대 토큰 수
        temperature=0.7,  # 응답의 창의성 조정
        n=3
    )

    # 응답에서 생성된 텍스트 반환
    return response.choices[0].message['content'].strip()

# 사용 예시
prompt = "너와 100일째인데 뭐하는게 좋을지 간략하게 추천해줘!"
output = ask_chatgpt(prompt)
print(output)


print(output)
