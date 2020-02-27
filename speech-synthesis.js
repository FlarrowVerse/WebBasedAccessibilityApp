function readText() {
	if('speechSynthesis' in window) with(speechSynthesis) {
		utterance = new SpeechSynthesisUtterance(document.querySelector('article').textContent);
		utterance.voice = getVoices()[0];
		speak(utterance);
	}else {
		document.querySelector('article').innerHTML = 'Not possible';
	}
}