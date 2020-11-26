from embedding_as_service_client import EmbeddingClient
# 가장 기본적인 LogisticRegression 을 사용합니다.
from sklearn.linear_model import LogisticRegression

# host 의 주소와 port 는 변경하시면 서버와 소통이 안 됩니다.
en = EmbeddingClient(host='54.180.124.154', port=8989)
print('Connected with server')
print('-' * 40)

# X_1, X_2, y_1, y_2 를 각각 임의로 설정해줍니다.

X_1 = ['banana is yellow', 'apple is red', 'orange is orange']

X_2 = ['driving a car', 'riding a bike']

Y_1 = 'fruits'

Y_2 = 'transportation'

# 설정이 따로 안되어 있는 LogisticRegression 을 사용해 위 값들을 하나로 합쳐 모델을 만들어봅니다.
classifier = LogisticRegression()

# 먼저 각각의 X_1, X_2 를 벡터화 하기 위해 다음과 같이 실행합니다.
em_X_1 = en.encode(texts=X_1)
em_X_2 = en.encode(texts=X_2)
print('> Complete encoding X values')
# print(em_X_1)


def append_to_with_label(to_arr, from_arr, label_arr, label):
    """
    from_arr 리스트에 있는 항목들을 to_arr 리스트에 append 하고
    레이블도 같이 추가해주는 함수입니다.
    """

    """
    1.  X = ['banana is yellow']
        y = ['fruits']
    2.  X = ['banana is yellow', 'apple is red']
        y = ['fruits', 'fruits']
    3.  X = ['banana is yellow', 'apple is red', 'orange is orange']
        y = ['fruits', 'fruits', 'fruits']
    """
    """
    1.  X = ['banana is yellow', 'apple is red', 'orange is orange', 'driving a car']
        y = ['fruits', 'fruits', 'fruits', 'transportation']
    2.  X = ['banana is yellow', 'apple is red', 'orange is orange', 'driving a car', 'riding a bike']
        y = ['fruits', 'fruits', 'fruits', 'transportation', 'transportation']
    """

    for item in from_arr:
        to_arr.append(item)
        label_arr.append(label)

# X 와 y 리스트를 새로 생성해 각각의 값을 하나로 묶어줍니다.
X = []
y = []

# 각각의 X_1, X_2 를 X 에 추가하고 y_1, y_2 의 레이블도 알맞게 추가해줍니다.
append_to_with_label(X, em_X_1, y, Y_1)
append_to_with_label(X, em_X_2, y, Y_2)
print('> Merging lists together')
# print(len(X))
# print(y)

# X, y 에 대한 리스트 추가가 끝난 뒤에는 해당 벡터들과 레이블을 활용해 모델을 만듭니다.
classifier.fit(X, y)
print('> Creating model')

# predict 하기 위한 값을 전달합니다.
PREDICTION_TEXT = ['board an airplane']

# prediction_text 도 서버를 통해 벡터화를 해줍니다.
em_pred_val = en.encode(texts=PREDICTION_TEXT)
print('> Encoding text to predict')

# 마지막으로 결과를 모델을 통해 구하고 출력해 봅니다.
pred_result = classifier.predict(em_pred_val)

print()
print(f"The final prediction value for {PREDICTION_TEXT} is {pred_result}")
