class sumthread extends threads
{
    int arr[];
    int start,end;
    int sum;

    public sumthread(int arr[],int start,int end)
    {
        this.arr=arr;
        this.start=start;
        this.end=end;
    }
    public void run()
    {
        sum=0;
        for (int i =start i <end; i++)
        {
            sum=sum+arr[i];
        }       
    }
    public int getsum()
    {
        return sum;
    }
}

public class threadeg{
    public static void main(String[] args) {
         int[] n={1,2,3,4,5,6};
         int mid=n.length/2;
         sumthread t1=new sumthread(n,0,mid);
         sumthread t2=new sumthread(n,mid,n.length);
         t1.start();
         t2.start();
         t1.join();
         t2.join();
         int totalsum = t1.getsum()+t2.getsum();

         System.out.println("sum of firsthalf" + t1.getsum());
         System.out.println("sum of secondhalf"+ t2.getsum());
         System.out.println("total sum"+ totalsum); 
    }
}