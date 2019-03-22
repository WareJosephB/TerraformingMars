
public final class Player {

	
	private int TR; //terraforming rating
	
	//should probably use class hierachy for resources but cba right now, just adding basic functionality
	private int heatProd;
	
	public Player() {
		// TODO Auto-generated constructor stub
		this.TR=0;
		this.heatProd=0;
	}

	//get setters
	public int getTR(){
		return this.TR;
	}
	public void TRchange(int amount){//dont shout at my awful naming conventions here, it's late and I can't think of anything better
		this.TR+=amount;
	}
	
	public int getHeatProd(){
		return this.heatProd;
	}
	public void heatProdchange(int amount){
		this.heatProd+=amount;
	}
}
