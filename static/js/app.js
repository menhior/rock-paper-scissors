const game = () => {
	let pScore = 0;
	let cScore = 0;
	let stats = {'playerStats': {'rock': 0, 'paper': 0, 'scissors': 0}, 'pScore': 0, 'cScore': 0, 'tie':0}

	const startGame = () =>{
		const playBtn = document.querySelector('.intro button')
		const introScreen = document.querySelector('.intro')
		const match = document.querySelector('.match')

		playBtn.addEventListener('click', () =>{
			introScreen.classList.add('fadeOut');
			match.classList.add('fadeIn')
		});
	};
	//Play game
	const playMatch = () => {
		const options = document.querySelectorAll('.options button');
		const playerHand = document.querySelector('.player-hand');
		const computerHand = document.querySelector('.computer-hand');
		const hands = document.querySelectorAll('.hands img');

		hands.forEach(hand =>{
			hand.addEventListener('animationend', function(){
				this.style.animation = '';
			})
		})
		// computer options
		const computerOptions = ['rock', 'paper', 'scissors'];

		options.forEach(option => {
			option.addEventListener('click', function(){
				//Computer Choice
				const computerNumber = Math.floor(Math.random() * 3);
				const computerChoice = computerOptions[computerNumber];
				setTimeout(() =>{
					//Here I call compareHands
					compareHands(this.textContent, computerChoice);
					//Update images
					playerHand.src = picDictionary[this.textContent];
					computerHand.src = picDictionary[computerChoice];
					}, 2000);

					playerHand.style.animation = "shakePlayer 2s ease";
					computerHand.style.animation = "shakeComputer 2s ease"
			});
		});

		const updateScore = () => {
			const playerScore = document.querySelector('.player-score p');
			const computerScore = document.querySelector('.computer-score p');
			playerScore.textContent = pScore;
			computerScore.textContent = cScore;
			stats['pScore'] = pScore;
			stats['cScore'] = cScore;
			document.cookie ='stats=' + JSON.stringify(stats) + ";domain=;path=/"
		}

		const compareHands = (playerChoice, computerChoice) =>{
			const winner = document.querySelector('.winner')
			//Checking for a tie
			if(playerChoice === 'rock'){
				stats['playerStats']['rock'] +=1;
			}else if(playerChoice === 'scissors'){
				stats['playerStats']['scissors'] += 1;
			}else{
				stats['playerStats']['paper'] +=1;
			}

			

			if(playerChoice === computerChoice){
				winner.textContent = 'It is a tie';
				stats['tie'] +=1;
				return;
			}
			//Checking for a rock
			if(playerChoice === 'rock'){
				if(computerChoice === 'scissors'){
					winner.textContent = 'Player Wins';
					pScore++;
					updateScore();
					return;
				}else{
					winner.textContent = 'Computer Wins';
					cScore++;
					updateScore();
					return;
				}
			};

			//Check for scissors
			if(playerChoice === 'scissors'){
				if(computerChoice === 'paper'){
					winner.textContent = 'Player Wins';
					pScore++;
					updateScore();
					return;
				}else{
					winner.textContent = 'Computer Wins';
					cScore++;
					updateScore();
					return;
				}
			};

			if(playerChoice === 'paper'){
				if(computerChoice === 'rock'){
					winner.textContent = 'Player Wins';
					pScore++;
					updateScore();
					return;
				}else{
					winner.textContent = 'Computer Wins';
					cScore++;
					updateScore();
					return;
				}
			};
		}
		document.cookie ='stats=' + JSON.stringify(stats) + ";domain=;path=/"

		
	};

	//call all the inner functions
	startGame();
	playMatch();

	

	console.log('Statistics for the game:', stats)
};

game();



