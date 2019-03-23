
public class Resource {
//create separate object for the different resources, hence no need for a name variable
	

	private int quant;
	private int prod;
	private int val;//is this for when paying for certain items, maybe this should be more complex than an integer in that case - C
	
	public Resource(int quantity,int production, int value) {
		// TODO Auto-generated constructor stub
		this.quant=quantity;
		this.prod=production;
		this.val=value;
	}
	
	public Resource(Corporation corp){
		/*
		 * For easy initialisation of Player class
		 * Try not to initialise a Corporation object this way
		 *
		 */
		
		
	}

	public int getQuantity(){
		return this.quant;
	}
	public boolean spend(int amount){//thought this might be a clever way to achieve this but might want to put logic somewhere else - C
		if (getQuantity()>amount){
			this.quant-=amount;
			return true;
		}else{
			return false;
		}
	}
	public void gain(int amount){//need to make sure this value is always positive, not sure where best to put logic for this - C
		this.quant+=amount;
	}
	
	public int getProduction(){
		return this.prod;
	}
	public void productionChange(int amount){
		this.prod+=amount;
	}
	
	public int getValue(){
		return this.val;
	}
	public void valueChange(int amount){
		this.val+=amount;
	}
}
