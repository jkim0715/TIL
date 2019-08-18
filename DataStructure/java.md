알고리즘 

ArrayList

- ```java
  ArrayList <Integer> list = new ArrayList<>();
  ```



Stack

- ```java
  Stack s = new Stack();
  
  //insert
  s.push();
  s.push();
  
  //check empty
  while(!s.isEmpty()){
      //pull out    
      System.out.println(s.pop());
  }
  ```

- 

Queue (FIFO)

- ```java
  Queue q = new LinkedList();
  
  // Insert
  q.offer("1");
  q.offer("1");
  q.offer("1");
  
  //check Empty
  while(!q.isEmpty()){
      //Pull out 
      System.out.println(q.poll());
  }
  ```

- Ex) Bridge w/ trucks

  ```java
  import java.util.LinkedList;
  import java.util.Queue;
  public class Truck {
  
  	public int solution(int bridge_length, int weight, int[] truck_weights) {
          int answer = 0;
          int sum = 0;
          Queue queue = new LinkedList<>();
          
          // initialise
          for(int i = 0; i < bridge_length; i++)
          	queue.add(0);
  
          for(int i = 0; i < truck_weights.length; i++) {
          	sum -= queue.poll();
  
          	if(sum + truck_weights[i] <= weight) { 
          		queue.add(truck_weights[i]);
          		sum += truck_weights[i];
          	}else {
          		queue.add(0);
          		i--;
          	}
          	answer++;
          }
          
          return answer + bridge_length;
      }
  } 
  ```


- EX) Max Number

  ```java
  import java.util.*;
  
  class Solution {
      public String solution(int[] numbers) {
          String answer = "";
      int temp =0;
          
          PriorityQueue<String> queue1 = new PriorityQueue<String>(new Comparator<String>(){
              @Override
              public int compare(String o1, String o2){
                  if(Integer.valueOf(o1+o2) > Integer.valueOf(o2+o1))
                      return -1;
                  else
                      return 1;
              }
          });      
          StringBuffer buffer =new StringBuffer();
          for(int i=0; i<numbers.length; i++){
              temp += numbers[i];
              queue1.add(String.valueOf(numbers[i]));
          }      
          while(!queue1.isEmpty()){
              String a = queue1.poll();
              buffer.append(a);
          }         
          if(temp==0)return "0";
          return buffer.toString();
      }
  }
  ```

  



