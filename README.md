# kogpt_chatbot

## kogpt2 원리(여기서 사용한)
- QA쌍을 받아서 다음 단어를 예측하는 방식(이때 A는 처음에 빈칸으로 시작)
  ```python
  input_ids=torch.LongTensor(tok.encode(U_TKN+q+SENT+sent+S_TKN+a)).unsqueeze(dim=0)
  pred=self(input_ids)
  ```
- torch.topk 함수 이용(k=3)
  - 문장생성시 가장 높은 확률의 3개에 대한 **확률값**과 그에 해당하는 **단어**를 출력하도록 함
  
- A(답변) 업데이트
  - 생성값 중 가장 확률이 높은 값(아래 예시에서 gen)을 추가해줌
  
## 결과 예시
### (prob=>확률, (gen,gen1,gen2)=> 순서대로 가장 높은 확률로 생성한 단어)
![image](https://user-images.githubusercontent.com/103883786/204030888-4f003af5-ba94-4a29-9293-fc70abf4ea3e.png)
![image](https://user-images.githubusercontent.com/103883786/204030912-7e9efac2-b91c-48a0-875f-6b49b6d637c2.png)
![image](https://user-images.githubusercontent.com/103883786/204030929-b2f7ca92-adc3-47ba-80df-fe5e2dacd601.png)

두번째 예시를 보면 1순위로 '저는', 2순위로 '저도', 3순위로 '저와'로 단어가 생성된 것을 볼 수 있다.

## 참고자료
https://github.com/haven-jeon/KoGPT2-chatbot


  
 
