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

  - LinkedList  구현 코드

    - ```java
      package list.linkedlist.implementation;
       
      public class LinkedList {
          // 첫번째 노드를 가리키는 필드
          private Node head;
          private Node tail;
          private int size = 0;
          private class Node{
              // 데이터가 저장될 필드
              private Object data;
              // 다음 노드를 가리키는 필드
              private Node next;
              public Node(Object input) {
                  this.data = input;
                  this.next = null;
              }
              // 노드의 내용을 쉽게 출력해서 확인해볼 수 있는 기능
              public String toString(){
                  return String.valueOf(this.data);
              }
          }
          public void addFirst(Object input){
              // 노드를 생성합니다.
              Node newNode = new Node(input);
              // 새로운 노드의 다음 노드로 해드를 지정합니다.
              newNode.next = head;
              // 헤드로 새로운 노드를 지정합니다.
              head = newNode;
              size++;
              if(head.next == null){
                  tail = head;
              }
          }
          public void addLast(Object input){
              // 노드를 생성합니다.
              Node newNode = new Node(input);
              // 리스트의 노드가 없다면 첫번째 노드를 추가하는 메소드를 사용합니다.
              if(size == 0){
                  addFirst(input);
              } else {
                  // 마지막 노드의 다음 노드로 생성한 노드를 지정합니다.
                  tail.next = newNode;
                  // 마지막 노드를 갱신합니다.
                  tail = newNode;
                  // 엘리먼트의 개수를 1 증가 시킵니다.
                  size++;
              }
          }
          Node node(int index) {
              Node x = head;
              for (int i = 0; i < index; i++)
                  x = x.next;
              return x;
          }
          public void add(int k, Object input){
              // 만약 k가 0이라면 첫번째 노드에 추가하는 것이기 때문에 addFirst를 사용합니다.
              if(k == 0){
                  addFirst(input);
              } else {
                  Node temp1 = node(k-1);
                  // k 번째 노드를 temp2로 지정합니다.
                  Node temp2 = temp1.next;
                  // 새로운 노드를 생성합니다.
                  Node newNode = new Node(input);
                  // temp1의 다음 노드로 새로운 노드를 지정합니다.
                  temp1.next = newNode;
                  // 새로운 노드의 다음 노드로 temp2를 지정합니다.
                  newNode.next = temp2;
                  size++;
                  // 새로운 노드의 다음 노드가 없다면 새로운 노드가 마지막 노드이기 때문에 tail로 지정합니다.
                  if(newNode.next == null){
                      tail = newNode;
                  }
              }
          }
          public String toString() {
              // 노드가 없다면 []를 리턴합니다.
              if(head == null){
                  return "[]";
              }       
              // 탐색을 시작합니다.
              Node temp = head;
              String str = "[";
              // 다음 노드가 없을 때까지 반복문을 실행합니다.
              // 마지막 노드는 다음 노드가 없기 때문에 아래의 구문은 마지막 노드는 제외됩니다.
              while(temp.next != null){
                  str += temp.data + ",";
                  temp = temp.next;
              }
              // 마지막 노드를 출력결과에 포함시킵니다.
              str += temp.data;
              return str+"]";
          }
          public Object removeFirst(){
              // 첫번째 노드를 temp로 지정하고 head의 값을 두번째 노드로 변경합니다.
              Node temp = head;
              head = temp.next;
              // 데이터를 삭제하기 전에 리턴할 값을 임시 변수에 담습니다. 
              Object returnData = temp.data;
              temp = null;
              size--;
              return returnData;
          }
          public Object remove(int k){
              if(k == 0)
                  return removeFirst();
              // k-1번째 노드를 temp의 값으로 지정합니다.
              Node temp = node(k-1);
              // 삭제 노드를 todoDeleted에 기록해 둡니다. 
              // 삭제 노드를 지금 제거하면 삭제 앞 노드와 삭제 뒤 노드를 연결할 수 없습니다.  
              Node todoDeleted = temp.next;
              // 삭제 앞 노드의 다음 노드로 삭제 뒤 노드를 지정합니다.
              temp.next = temp.next.next;
              // 삭제된 데이터를 리턴하기 위해서 returnData에 데이터를 저장합니다.
              Object returnData = todoDeleted.data; 
              if(todoDeleted == tail){
                  tail = temp;
              }
              // cur.next를 삭제 합니다.
              todoDeleted = null; 
              size--;
              return returnData;
          }
          public Object removeLast(){
              return remove(size-1);
          }
          public int size(){
              return size;
          }
          public Object get(int k){
              Node temp = node(k);
              return temp.data;
          }
          public int indexOf(Object data){
              // 탐색 대상이 되는 노드를 temp로 지정합니다.
              Node temp = head;
              // 탐색 대상이 몇번째 엘리먼트에 있는지를 의미하는 변수로 index를 사용합니다.
              int index = 0;
              // 탐색 값과 탐색 대상의 값을 비교합니다. 
              while(temp.data != data){
                  temp = temp.next;
                  index++;
                  // temp의 값이 null이라는 것은 더 이상 탐색 대상이 없다는 것을 의미합니다.이 때 -1을 리턴합니다.
                  if(temp == null)
                      return -1;
              }
              // 탐색 대상을 찾았다면 대상의 인덱스 값을 리턴합니다.
              return index;
          }
       
          // 반복자를 생성해서 리턴해줍니다.
          public ListIterator listIterator() {
              return new ListIterator();
          }
           
          class ListIterator{
              private Node lastReturned;
              private Node next;
              private int nextIndex;
               
              ListIterator(){
                  next = head;
                  nextIndex = 0;
              }
               
              // 본 메소드를 호출하면 next의 참조값이 기존 next.next로 변경됩니다. 
              public Object next() {
                  lastReturned = next;
                  next = next.next;
                  nextIndex++;
                  return lastReturned.data;
              }
               
              public boolean hasNext() {
                  return nextIndex < size();
              }
               
              public void add(Object input){
                  Node newNode = new Node(input);
                  if(lastReturned == null){
                      head= newNode;
                      newNode.next = next;
                  } else {
                      lastReturned.next = newNode;
                      newNode.next = next;
                  }
                  lastReturned = newNode;
                  nextIndex++;
                  size++;
              }
               
              public void remove(){
                  if(nextIndex == 0){
                      throw new IllegalStateException();
                  }
                  LinkedList.this.remove(nextIndex-1);
                  nextIndex--;
              }
               
          }
       
      }
      ```

-  Dubly Linked List

  - 구현 코드

    - ```java
      package list.doublylinkedlist.implementation;
       
      public class DoublyLinkedList {
          // 첫번째 노드를 가리키는 필드
          private Node head;
          private Node tail;
          private int size = 0;
       
          private class Node {
              // 데이터가 저장될 필드
              private Object data;
              // 다음 노드를 가리키는 필드
              private Node next;
              private Node prev;
       
              public Node(Object input) {
                  this.data = input;
                  this.next = null;
                  this.prev = null;
              }
       
              // 노드의 내용을 쉽게 출력해서 확인해볼 수 있는 기능
              public String toString() {
                  return String.valueOf(this.data);
              }
          }
       
          public void addFirst(Object input) {
              // 노드를 생성합니다.
              Node newNode = new Node(input);
              // 새로운 노드의 다음 노드로 헤드를 지정합니다.
              newNode.next = head;
              // 기존에 노드가 있었다면 현재 헤드의 이전 노드로 새로운 노드를 지정합니다.
              if (head != null)
                  head.prev = newNode;
              // 헤드로 새로운 노드를 지정합니다.
              head = newNode;
              size++;
              if (head.next == null) {
                  tail = head;
              }
          }
       
          public void addLast(Object input) {
              // 노드를 생성합니다.
              Node newNode = new Node(input);
              // 리스트의 노드가 없다면 첫번째 노드를 추가하는 메소드를 사용합니다.
              if (size == 0) {
                  addFirst(input);
              } else {
                  // tail의 다음 노드로 생성한 노드를 지정합니다.
                  tail.next = newNode;
                  // 새로운 노드의 이전 노드로 tail을 지정합니다.
                  newNode.prev = tail;
                  // 마지막 노드를 갱신합니다.
                  tail = newNode;
                  // 엘리먼트의 개수를 1 증가 시킵니다.
                  size++;
              }
          }
       
          Node node(int index) {
              // 노드의 인덱스가 전체 노드 수의 반보다 큰지 작은지 계산
              if (index < size / 2) {
                  // head부터 next를 이용해서 인덱스에 해당하는 노드를 찾습니다.
                  Node x = head;
                  for (int i = 0; i < index; i++)
                      x = x.next;
                  return x;
              } else {
                  // tail부터 prev를 이용해서 인덱스에 해당하는 노드를 찾습니다.
                  Node x = tail;
                  for (int i = size - 1; i > index; i--)
                      x = x.prev;
                  return x;
              }
          }
       
          public void add(int k, Object input) {
              // 만약 k가 0이라면 첫번째 노드에 추가하는 것이기 때문에 addFirst를 사용합니다.
              if (k == 0) {
                  addFirst(input);
              } else {
                  Node temp1 = node(k - 1);
                  // k 번째 노드를 temp2로 지정합니다.
                  Node temp2 = temp1.next;
                  // 새로운 노드를 생성합니다.
                  Node newNode = new Node(input);
                  // temp1의 다음 노드로 새로운 노드를 지정합니다.
                  temp1.next = newNode;
                  // 새로운 노드의 다음 노드로 temp2를 지정합니다.
                  newNode.next = temp2;
                  // temp2의 이전 노드로 새로운 노드를 지정합니다.
                  if (temp2 != null)
                      temp2.prev = newNode;
                  // 새로운 노드의 이전 노드로 temp1을 지정합니다.
                  newNode.prev = temp1;
                  size++;
                  // 새로운 노드의 다음 노드가 없다면 새로운 노드가 마지막 노드이기 때문에 tail로 지정합니다.
                  if (newNode.next == null) {
                      tail = newNode;
                  }
              }
          }
       
          public String toString() {
              // 노드가 없다면 []를 리턴합니다.
              if (head == null) {
                  return "[]";
              }
              // 탐색을 시작합니다.
              Node temp = head;
              String str = "[";
              // 다음 노드가 없을 때까지 반복문을 실행합니다.
              // 마지막 노드는 다음 노드가 없기 때문에 아래의 구문은 마지막 노드는 제외됩니다.
              while (temp.next != null) {
                  str += temp.data + ",";
                  temp = temp.next;
              }
              // 마지막 노드를 출력결과에 포함시킵니다.
              str += temp.data;
              return str + "]";
          }
       
          public Object removeFirst() {
              // 첫번째 노드를 temp로 지정하고 head의 값을 두번째 노드로 변경합니다.
              Node temp = head;
              head = temp.next;
              // 데이터를 삭제하기 전에 리턴할 값을 임시 변수에 담습니다.
              Object returnData = temp.data;
              temp = null;
              // 리스트 내에 노드가 있다면 head의 이전 노드를 null로 지정합니다.
              if (head != null)
                  head.prev = null;
              size--;
              return returnData;
          }
       
          public Object remove(int k) {
              if (k == 0)
                  return removeFirst();
              // k-1번째 노드를 temp로 지정합니다.
              Node temp = node(k - 1);
              // temp.next를 삭제하기 전에 todoDeleted 변수에 보관합니다.
              Node todoDeleted = temp.next;
              // 삭제 대상 노드를 연결에서 분리합니다.
              temp.next = temp.next.next;
              if (temp.next != null) {
                  // 삭제할 노드의 전후 노드를 연결합니다.
                  temp.next.prev = temp;
              }
              // 삭제된 노드의 데이터를 리턴하기 위해서 returnData에 데이터를 저장합니다.
              Object returnData = todoDeleted.data;
              // 삭제된 노드가 tail이었다면 tail을 이전 노드를 tail로 지정합니다.
              if (todoDeleted == tail) {
                  tail = temp;
              }
              // cur.next를 삭제 합니다.
              todoDeleted = null;
              size--;
              return returnData;
          }
       
          public Object removeLast() {
              return remove(size - 1);
          }
       
          public int size() {
              return size;
          }
       
          public Object get(int k) {
              Node temp = node(k);
              return temp.data;
          }
       
          public int indexOf(Object data) {
              // 탐색 대상이 되는 노드를 temp로 지정합니다.
              Node temp = head;
              // 탐색 대상이 몇번째 엘리먼트에 있는지를 의미하는 변수로 index를 사용합니다.
              int index = 0;
              // 탐색 값과 탐색 대상의 값을 비교합니다.
              while (temp.data != data) {
                  temp = temp.next;
                  index++;
                  // temp의 값이 null이라는 것은 더 이상 탐색 대상이 없다는 것을 의미합니다.이 때 -1을 리턴합니다.
                  if (temp == null)
                      return -1;
              }
              // 탐색 대상을 찾았다면 대상의 인덱스 값을 리턴합니다.
              return index;
          }
       
          // 반복자를 생성해서 리턴해줍니다.
          public ListIterator listIterator() {
              return new ListIterator();
          }
       
          public class ListIterator {
              private Node lastReturned;
              private Node next;
              private int nextIndex;
       
              ListIterator() {
                  next = head;
                  nextIndex = 0;
              }
       
              // 본 메소드를 호출하면 cursor의 참조값이 기존 cursor.next로 변경됩니다.
              public Object next() {
                  lastReturned = next;
                  next = next.next;
                  nextIndex++;
                  return lastReturned.data;
              }
       
              // cursor의 값이 없다면 다시 말해서 더 이상 next를 통해서 가져올 노드가 없다면 false를 리턴합니다.
              // 이를 통해서 next를 호출해도 되는지를 사전에 판단할 수 있습니다.
              public boolean hasNext() {
                  return nextIndex < size();
              }
       
              public boolean hasPrevious() {
                  return nextIndex > 0;
              }
       
              public Object previous() {
                  if (next == null) {
                      lastReturned = next = tail;
                  } else {
                      lastReturned = next = next.prev;
                  }
                  nextIndex--;
                  return lastReturned.data;
              }
       
              public void add(Object input) {
                  Node newNode = new Node(input);
                  if (lastReturned == null) {
                      head = newNode;
                      newNode.next = next;
                  } else {
                      lastReturned.next = newNode;
                      newNode.prev = lastReturned;
                      if (next != null) {
                          newNode.next = next;
                          next.prev = newNode;
                      } else {
                          tail = newNode;
                      }
                  }
                  lastReturned = newNode;
                  nextIndex++;
                  size++;
              }
       
              public void remove() {
                  if (nextIndex == 0) {
                      throw new IllegalStateException();
                  }
                  Node n = lastReturned.next;
                  Node p = lastReturned.prev;
       
                  if (p == null) {
                      head = n;
                      head.prev = null;
                      lastReturned = null;
                  } else {
                      p.next = next;
                      lastReturned.prev = null;
                  }
       
                  if (n == null) {
                      tail = p;
                      tail.next = null;
                  } else {
                      n.prev = p;
                  }
       
                  if (next == null) {
                      lastReturned = tail;
                  } else {
                      lastReturned = next.prev;
                  }
       
                  size--;
                  nextIndex--;
       
              }
          }
       
      }
      ```

    - 

 



set 

-  집합

graph

-  최단거리 

