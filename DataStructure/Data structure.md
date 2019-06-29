# Data structure

Purpose? 

현실 세계의 일을 프로그래밍적으로 구현하기 편하게 하기위하여 사용



중요한 특징

- 거대한 데이터를 효율적으로 관리하는 것.



정리 정돈의 진화

문서 - 책 -책장 - 도서관 - 인터넷



공부법

대전제 

- 몰라도 프로그램을 만들 수 있다.



Data Structure lecture Using Java

1. 배열 [Array]

   - 여러 데이터를 하나의 이름으로 그루핑해서 관리하기위한 데이터 스트럭쳐
   - element
     - value
     - index
   - 데이터 추가시 기존의 인덱스에 있던  value에 덮어 씌워진다
   - 데이터 제거시 해당 인덱스의   value 는 비워진다.

2. List

   - 순서를 가지고 있다.

   - 중복을 허용한다.

   - 데이터를 추가하면 기존에 있던 인덱스는 한칸 뒤로 밀린다.

   - 데이터를 지워도 뒤에있던 데이터가 한칸씩 앞으로 온다.

   - 리스트 기능

     - 처음 끝 중간에 엘리먼트를 추가/삭제하는 기능

     - 리스트에 데이터가 있는지를 체크하는 기능

     - 리스트의 모든데이터에 접근 가능. 

       - |            | 추가/삭제 | 조회 |
         | ---------- | --------- | ---- |
         | ArrayList  | 느림      | 빠름 |
         | LinkedList | 빠름      | 느림 |

     

- Array vs List 
  - Array 는 index가 중요하게 여겨지고
  - List 는 순서가 중요하게 여겨진다.



- ArrayLIst 

  - 값을 추가할때 끝에서부터 한칸씩 밀어서 빈공간을 만든다.

  - 값을 삭제할때 삭제하고 모든 데이터들을 뒤에서 한칸씩 앞으로 떙낀다.

  - 사용법:

    - ```
      ArrayList<Integer> list = new ArrayList<>;
      list.add(10);
      list.add(20);
      list.add(30);
      list.add(2.25);
      
      list.remove();
      list.pull();
      list.size();
      
      ```

      반복문을 이용한 ArrayList생성 (Iterator, for문)

    - ``` java
      Iterator it = list.iterator();
      while(it.hasNext()){	//.hasNext() Boolean 값 리턴
          int value = (int)it.next(); //.next(); Value값 리턴(Object type)
      }
      // or
      for(int value:numbers){
          System.out.println(value);
      }
      // or
      for(int i=0; i<list.size(); i++){
          System.out.println(list.get(i));
      }
      ```

      

  



 



set 

-  집합

graph

-  최단거리 

