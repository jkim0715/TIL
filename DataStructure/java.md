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

- ```java
  package programmers;
  
  public class Stock {
  
  	public static void main(String[] args) {
  	int [] prices = {1,2,3,2,3};
  	int [] answer = new int [prices.length];
  	int p =0;
  	int cnt=0;
  	while(true) {
  		
  		for(int i=p+1; i<prices.length-1;i++ ) {
  		
  			if(prices[p] <= prices[i]) {
  				cnt++;
  			
  			}if(prices[p] > prices[i]) {
  				cnt++;
  				answer[p] = cnt;
  				cnt =0;
  				break;
  			}if(i == prices.length-2) {
  				answer[p] = cnt+1;
  				cnt=0;
  				break;
  			}
  			
  		}
  		if(p==prices.length-2) {
  			answer[p] = 1;
  		}
  		if(p==prices.length-1 ) {
  			answer[p] = 0;
  			break;
  		}
  		p++;
  	}
  	for(int i=0; i<answer.length;i++) {
  		System.out.println(answer[i]);
  	}
  	
  	
  	}
  
  }
  ```

-  

DFS/BFS

- ```java
  public class TargetValue {
      
      
      public static void main(String[] args) {
          int [] numbers = {1,1,1,1,1} ;
          int target = 3 ;
          
          dfs(numbers,target,0,0);
          System.out.println(dfs(numbers,target,0,0));
      }
   
      
      public static int dfs(int [] numbers, int target, int depth,int pnum) {
          
          int ans = 0;
          if(depth == numbers.length) {
              if( pnum == target) {
          
              return 1; 
              }
              else {
                  return 0;
              }
          }
          ans += dfs(numbers, target, depth+1, pnum + numbers[depth]);
          ans += dfs(numbers, target, depth+1, pnum - numbers[depth]);
   
          return ans;    
      }
  }
  ```

- 



