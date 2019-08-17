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

  