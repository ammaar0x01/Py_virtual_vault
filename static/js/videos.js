/*
videos.js
=========
Started: (04.05.25; based on previous project from "1x.04.25")
Updated: 04.05.25
=========
*/


/**
 * Getting all youtube links from the HTML page, 
 * then adding them to an local-variable array,  
 * finally returns the array of youtube-video links
 * 
 * @returns {string[]} An array of YouTube video links
 * 
*/
function getYouTubeLinks() {
  let videoYoutubeLinks = []
  let videoYoutubeLinksContainer = document.getElementsByClassName("youtube-video-link")
  for (let a = 0; a < videoYoutubeLinksContainer.length; a++) {
    videoYoutubeLinks.push(videoYoutubeLinksContainer[a].href)
  }
  return videoYoutubeLinks

}
// ---------------------------------

/**
 * Extracts the video id from a youtube-video URL
 * 
 * @returns {string} A youtube-video id || "invalid URL" || "invalid id"
*/
function URLtoVideoId(videoURL) {
  const isValidURL = videoURL.includes("https://www.youtube.com");
  if (!isValidURL) {
    return "invalid URL";
  }

  let videoId = "";
  const isShort = videoURL.includes("shorts");
  if (isShort) {
    videoId = videoURL.substring(31, videoURL.length).trim();
  } 
  else {
    // 'pure' url
    videoId = videoURL.substring(32, videoURL.length).trim();
  }

  if (videoId.length == 11){
    return videoId
  }
  return "invalid id"
}
// --------------------------------

let videoIds = []
/**
 * Extracting video-ids and adding them to an array
*/
function convertAndAddVideo(){
  for (let a = 0; a < videoLinks.length; a++) {
    if (videoLinks[a] != "") {
      let videoId = URLtoVideoId(videoLinks[a]);
      if (videoId != "invalid URL" || videoId != "invalid id") {
        videoIds.push(videoId);
      }
    }
    // else {
    //   console.log("empty string");
    // }
  }
}
// --------------------------------


/**
 * Adds a youtube-iframe URL to an iframe, 
 * and displays the iframe on the HTML webpage 
 * 
 * @param {string} YouTubeEmbedURL - A youtube-iframe URL
*/
function addURLtoIFrame(YouTubeEmbedURL) {
  const iframeSection = document.getElementById("inner");
  let iFrameMain = `
    <!-- from videos.js-->
    <iframe 
        src="${YouTubeEmbedURL}"
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen>
    </iframe>

    <br />
    <div id="iframe-yt"></div>
    `;
  iframeSection.innerHTML = iFrameMain;
}
// ---------------------------------

/**
 * Adds a youtube-video id to an youtube-iframe URL
 * 
 * @param {string} videoId - A youtube-video id 
 * @returns {string} baseEmbedURL; A complete youtube-iframe URL
*/
function videoIdToURL(videoId) {
  let baseEmbedURL = `https://www.youtube.com/embed/${videoId}?si=TMkLTDEoY0WWFON6`;
  return baseEmbedURL;
}
// --------------------------------


const buttons = document.getElementsByClassName("iframe-btn");
/**
 * Adds click-events to buttons that share the same class-name
*/
function addEventToButtons() {
  console.log("\nAdding button events...")
  for (let a = 0; a < videoIds.length; a++) {
    buttons[a].addEventListener("click", () => {
      let videoURL = videoIdToURL(videoIds[a]);
      addURLtoIFrame(videoURL);
    });
    console.log(a, "event added");
  }
}
// ---------------------------------


// ===================================
// Running all necessary functions 

let videoLinks = getYouTubeLinks()
convertAndAddVideo()
addEventToButtons()
// ===================================
