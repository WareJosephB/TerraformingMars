
public final class Player {

	
	public Resource money;
	public Resource steel;
	public Resource titanium;
	public Resource plant;
	public Resource energy;
	public Resource heat;
	
	private Resource[] resources;//to make handling resources inside class easier
	
	private int TR; //terraforming rating
	

	public Player(Corporation corp) {
		// TODO Auto-generated constructor stub
		this.TR=0;

		resources=new Resource[]{money,steel,titanium,plant,energy,heat};//worth double checking I'm using this right, its been a while -C
		
		for (int i=0;i<resources.length;i++){
			resources[i]=new Resource(corp);
		}
	}

	//get setters
	public int getTR(){
		return this.TR;
	}
	public void TRchange(int amount){//dont shout at my awful naming conventions here, it's late and I can't think of anything better - C
		this.TR+=amount;
	}
	
	public void Update(){
		money.gain(getTR());//calculate money gain from TR separately
		for (int i=0;i<resources.length;i++){
			resources[i].gain(resources[i].getProduction());//if this is not the only place for a player to gain production then this should be absorbed into the resource class - C
		}
	}
	
}
