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

  - ArrayList 구현 전체 코드

    - ``` java
      package list.arraylist.implementation;
       
      public class ArrayList {
          private int size = 0;
          private Object[] elementData = new Object[100];
       
          public ArrayList() {
       
          }
           
          public boolean addLast(Object element) {
              elementData[size] = element;
              size++;
              return true;
          }
           
          public boolean add(int index, Object element) {
              // 엘리먼트 중간에 데이터를 추가하기 위해서는 끝의 엘리먼트부터 index의 노드까지 뒤로 한칸씩 이동시켜야 합니다.
              for (int i = size - 1; i >= index; i--) {
                  elementData[i + 1] = elementData[i];
              }
              // index에 노드를 추가합니다.
              elementData[index] = element;
              // 엘리먼트의 숫자를 1 증가 시킵니다.
              size++;
              return true;
          }
           
          public boolean addFirst(Object element){
              return add(0, element);
          }
       
          public String toString() {
              String str = "[";
              for (int i = 0; i < size; i++) {
                  str += elementData[i];
                  if (i < size - 1)
                      str += ",";
              }
              return str + "]";
          }
           
          public Object remove(int index) {
              // 엘리먼트를 삭제하기 전에 삭제할 데이터를 removed 변수에 저장합니다.
              Object removed = elementData[index];
              // 삭제된 엘리먼트 다음 엘리먼트부터 마지막 엘리먼트까지 순차적으로 이동해서 빈자리를 채웁니다.
              for (int i = index + 1; i <= size - 1; i++) {
                  elementData[i - 1] = elementData[i];
              }
              // 크기를 줄입니다.
              size--;
              // 마지막 위치의 엘리먼트를 명시적으로 삭제해줍니다. 
              elementData[size] = null;
              return removed;
          }   
           
          public Object removeFirst(){
              return remove(0);
          }
       
          public Object removeLast(){
              return remove(size-1);
          }
       
          public Object get(int index) {
              return elementData[index];
          }
       
          public int size() {
              return size;
          }
       
          public int indexOf(Object o) {
              for (int i = 0; i < size; i++) {
                  if (o.equals(elementData[i])) {
                      return i;
                  }
              }
              return -1;
          }
       
          public ListIterator listIterator() {
              // ListIterator 인스턴스를 생성해서 리턴합니다.
              return new ListIterator();
          }
       
           
       
          class ListIterator {
              // 현재 탐색하고 있는 순서를 가르키는 인덱스 값
              private int nextIndex = 0;
       
              // next 메소르를 호출할 수 있는지를 체크합니다.
              public boolean hasNext() {
                  // nextIndex가 엘리먼트의 숫자보다 적다면 next를 이용해서 탐색할 엘리먼트가 존재하는 것이기 때문에 true를 리턴합니다. 
                  return nextIndex < size();
              }
               
              // 순차적으로 엘리먼트를 탐색해서 리턴합니다. 
              public Object next() {
                  // nextIndex에 해당하는 엘리먼트를 리턴하고 nextIndex의 값을 1 증가 시킵니다.
                  return elementData[nextIndex++];
              }
               
              // previous 메소드를 호출해도 되는지를 체크합니다.
              public boolean hasPrevious(){
                  // nextIndex가 0보다 크다면 이전 엘리먼트가 존재한다는 의미입니다.
                  return nextIndex > 0;
              }
               
              // 순차적으로 이전 노드를 리턴합니다.
              public Object previous(){
                  // 이전 엘리먼트를 리턴하고 nextIndex의 값을 1감소합니다. 
                  return elementData[--nextIndex];
              }
               
              // 현재 엘리먼트를 추가합니다. 
              public void add(Object element){
                  ArrayList.this.add(nextIndex++, element);
              }
               
              // 현재 엘리먼트를 삭제합니다. 
              public void remove(){
                  ArrayList.this.remove(nextIndex-1);
                  nextIndex--;
              }
             
          }
       
      }
      ```

- LinkedList

  - 연결 !
  - 메모리란? 
    - 데이터 스트럭쳐의 미션은 메모리의 효율적 사용 !!!!

  



 



set 

-  집합

graph

-  최단거리 

