import java.util.ArrayList;
import java.util.List;

/**
 * Main class for all things apart from the game board and game loop
 * Holder and Board piece diverge here
 **/

public abstract class Entity {

	public static List<Entity> entities=null; //not sure if needed in entity
	
	public Entity() {
		// TODO Auto-generated constructor stub
		if (entities == null) entities = new ArrayList<>();
        entities.add(this);
		
	}

	public void NewRound(){}
	
	public void TurnStart(){}
	
	public void TurnEnd(){}
}