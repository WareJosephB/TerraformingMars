/**
 * Something capable of 'Holding' resources.
 * Card and Player diverge here
 */


public abstract class Holder extends Entity {

	
	public Resource money;
	public Resource steel;
	public Resource titanium;
	public Resource plant;
	public Resource energy;
	public Resource heat;
	
	protected Resource[] resources;
	
	/**
	 * 
	 */
	public Holder(Resource money, Resource steel, Resource titanium, Resource plant, Resource energy, Resource heat) {
		super();
		
		this.money=money;
		this.steel=steel;
		this.titanium=titanium;
		this.plant=plant;
		this.energy=energy;
		this.heat=heat;
		
		resources=new Resource[]{money,steel,titanium,plant,energy,heat};
	}

	/*
	public Holder(Resource[] resources){
		this(resources[0],resources[1],resources[2],resources[3],resources[4],resources[5]);
		
	}*/
}
