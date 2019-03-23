
public final class Board {
	// game board

	private int temp;// create up get setters
	private int tempMax;

	private int oceans;
	private int oceansMax;

	private int oxygen;
	private int oxygenMax;

	public Board(int tempMax, int oceanMax, int oxygenMax) {
		// TODO Auto-generated constructor stub
		this.temp = -30;
		this.tempMax = tempMax;

		this.oceans = 0;
		this.oceansMax = 0;

		this.oxygen = 0;
		this.oxygenMax = oxygenMax;
	}

	public void TempRaise(int raiseBy, Player player) {
		for (int i = 0; i < raiseBy; i++) {
			if (this.temp < this.tempMax) {
				this.temp += 2;
				player.TRchange(1);
				if (this.temp == -24 || this.temp == -20) {// would be a good idea to make the milestones not hard coded - C
					
					player.heat.productionChange(1);
					
				} else if (this.temp == 0) {

					/*
					not sure how best to implement giving player an ocean to place.
					should decide on flow of game.
					most likely need to implement method for player to place ocean before this can be implemented

					- C
					 */
					 
				}
			}
		}
	}
}
