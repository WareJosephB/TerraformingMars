
public abstract class Resource {
//create separate classes for the different resources, hence no need for a name variable
	
	//need dem get setters
	private int quant;
	private int prod;
	private int val;
	
	public Resource(int quantity,int production, int value) {
		// TODO Auto-generated constructor stub
		this.quant=quantity;
		this.prod=production;
		this.val=value;
	}

	public int getQuantity(){
		return this.quant;
	}
	public boolean spend(int amount){//thought this might be a clever way to acheive this but might want to put logic somewhere else
		if (getQuantity()>amount){
			this.quant-=amount;
			return true;
		}else{
			return false;
		}
	}
	public void gain(int amount){//need to make sure this value is always positive, not sure where best to put logic for this
		this.quant+=amount;
	}
	
	public void Production(){
		
	}
}
