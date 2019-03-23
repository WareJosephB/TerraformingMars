
public final class Player extends Holder{

	

	
	//to make handling resources inside class easier
	
	private int TR; //terraforming rating
	

	public Player(Corporation corp) {
		// TODO Auto-generated constructor stub
		super(corp.money, corp.steel, corp.titanium, corp.plant, corp.energy, corp.heat);
		
		this.TR=0;


	}

	//get setters
	public int getTR(){
		return this.TR;
	}
	public void TRchange(int amount){//dont shout at my awful naming conventions here, it's late and I can't think of anything better - C
		this.TR+=amount;
	}
	
	public void NewRound(){
		money.gain(getTR());//calculate money gain from TR separately
		for (int i=0;i<resources.length;i++){
			resources[i].gain(resources[i].getProduction());//if this is not the only place for a player to gain production then this should be absorbed into the resource class - C
		}
	}
	
	
}
