public class CircularQueue {
    private String[] queue;
    private int headPointer;
    private int tailPointer;
    private int numberOfItems;

    // Constructor to initialize the circular queue with a specified size
    public CircularQueue(int size) {
        queue = new String[size]; // create an array to hold the queue elements
        headPointer = 0;          // initialize head pointer
        tailPointer = 0;          // initialize tail pointer
        numberOfItems = 0;        // initialize item count
    }

    // Method to enqueue an item into the circular queue
    public boolean enqueue(String item) {
        // check if the queue is full
        if (numberOfItems >= queue.length) {
            System.out.println("Queue is full, cannot enqueue.");
            return false; // return false if the queue is full
        }

        // add item to the queue at tailPointer position
        queue[tailPointer] = item;

        // update tail pointer
        if (tailPointer == queue.length - 1) { // check if at end of queue
            tailPointer = 0; // wrap around to beginning
        } else {
            tailPointer++; // move to next index 
        }

        // increment number of items in the queue 
        numberOfItems++; 
        return true; // return true indicating successful enqueue 
    }

    // Method to dequeue an item from the circular queue
    public String dequeue() {
        // check if the queue is empty
        if (numberOfItems == 0) {
            System.out.println("Queue is empty, cannot dequeue.");
            return null; // return null if the queue is empty
        }

        // retrieve item at headPointer position
        String item = queue[headPointer];

        // clear position in the queue (optional)
        queue[headPointer] = null;

        // update head pointer
        if (headPointer == queue.length - 1) { // check if at end of queue
            headPointer = 0; // wrap around to beginning
        } else {
            headPointer++; // move to next index 
        }

        // decrement number of items in the queue 
        numberOfItems--; 
        return item; // return the dequeued item 
    }

    public static void main(String[] args) {
        CircularQueue cq = new CircularQueue(10); // create a circular queue of size 10 
        cq.enqueue("item1");                       // adds 'item1' to the queue 
        cq.enqueue("item2");                       // adds 'item2' to the queue 

        String dequeuedItem = cq.dequeue();       // removes and returns the item at the front of the queue 
        System.out.println("Dequeued: " + dequeuedItem); 

        // print the current state of the queue (for demonstration)
        for (String item : cq.queue) {
            System.out.print(item + " ");
        }
    }
}