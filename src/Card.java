import java.awt.Color;

public abstract class Card {

	/*
	 * might be better to do further object wonderfullness with resources and productions to streamline this huge list of variables
	 */
	
	private Resource money;
	private Resource steel;
	private Resource titanium;
	private Resource plant;
	private Resource energy;
	private Resource heat;
	
    private Color color;//better to keep with this spelling for consistency reasons - C
    private int price;
    private String name;
    private String tags;//not sure how best to handle this - C
    private String description; 

    private int oceanIncrease; 
    private int oxygenIncrease; 
    private int oxygenLimit; 
    private int oxygenDirection; // 0 = none, -1 = needs less than, +1 = more
    private int oceanLimit;
    private int oceanDirection ;// as above
    private int temperatureLimit;
    private int temperatureDirection;
	
	/*
	 * Good idea to make different classes for the different type of cards - C
	 */
	protected Card(String name, Color color, int Price, String tags,//constructor needs all the other stuff but I this can be handled better - C
				String description){
        this.color = color;
        this.price = price;
        this.name = name;
        this.tags = tags;
        this.description = description;
        //this.heatIncrease = 0;
        this.oceanIncrease = 0;
        this.oxygenIncrease = 0;
        /*this.moneyProd = 0;
        this.steelProd = 0;
        this.titaniumProd = 0;
        this.plantProd = 0;
        this.energyProd = 0;
        this.heatProd = 0;
        this.numMoney = 0;
        this.numSteel = 0;
        this.numTitanium = 0;
        this.numPlant = 0;
        this.numEnergy = 0;
        this.numHeat = 0;*/
        this.oxygenLimit = 0;
        this.oxygenDirection = 0; 
        this.oceanLimit = 0;
        this.oceanDirection = 0;  
        this.temperatureLimit = 0;
        this.temperatureDirection = 0;
	}

}
