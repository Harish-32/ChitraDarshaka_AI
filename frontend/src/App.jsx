import { useState } from "react";
import axios from "axios";
import Hi from "./compo/hi";

function App() {

  const [prompt, setPrompt] = useState("");
  const [language, setLanguage] = useState("English");

  const [story, setStory] = useState("");
  const [script, setScript] = useState("");
  const [videoUrl, setVideoUrl] = useState("");

  const [storyLoading, setStoryLoading] = useState(false);
  const [trailerLoading, setTrailerLoading] = useState(false);

  const buttonStyle = {
    background: "linear-gradient(135deg,#6a11cb,#2575fc)",
    color: "white",
    border: "none",
    padding: "15px 10px",
    fontSize: "18px",
    fontWeight: "bold",
    borderRadius: "8px",
    cursor: "pointer",
    boxShadow: "0px 4px 15px rgba(0,0,0,0.3)"
  };

  const cardStyle = {
    background: "white",
    padding: "20px",
    borderRadius: "10px",
    marginTop: "20px",
    boxShadow: "0px 4px 15px rgba(0,0,0,0.2)"
  };

  // STEP 1 - Generate Story

  const generateStory = async () => {

    if (!prompt.trim()) {
      alert("Please enter a movie idea");
      return;
    }

    setStoryLoading(true);

    try {

      const res = await axios.post(
        "http://localhost:8000/generate-story",
        {
          prompt,
          language
        }
      );

      setStory(res.data.story);

      setScript("");
      setVideoUrl("");

    } catch (err) {

      console.log(err);
      alert("Story Generation Failed");

    }

    setStoryLoading(false);
  };

  // STEP 2 - Generate Trailer

  const generateTrailer = async () => {

    setTrailerLoading(true);

    try {

      const res = await axios.post(
        "http://localhost:8000/generate-trailer",
        {
          story,
          language
        }
      );

      setScript(
        res.data.trailer_script
      );

      setVideoUrl(
        res.data.video
      );

    } catch (err) {

      console.log(err);
      alert("Trailer Generation Failed");

    }

    setTrailerLoading(false);
  };

  return (

    <div
      style={{
        minHeight: "100vh",
        background: "#000",
        padding: "40px"
      }}
    >

      <Hi name="welcome to" />

      <h1
        style={{
          textAlign: "center",
          color: "white",
          fontSize: "50px",
          marginBottom: "30px"
        }}
      >
        🎬 KathaChitra AI 
      </h1>

      <div
        style={{
          maxWidth: "1000px",
          margin: "auto",
          background: "#111",
          padding: "30px",
          borderRadius: "20px"
        }}
      >

        <h3 style={{ color: "white" }}>
          Movie Idea
        </h3>

        <textarea
          rows="6"
          value={prompt}
          onChange={(e) =>
            setPrompt(e.target.value)
          }
          placeholder="Enter movie idea..."
          style={{
            width: "100%",
            padding: "8px",
            borderRadius: "8px",
            fontSize: "16px"
          }}
        />

        <br />
        <br />

        <h3 style={{ color: "white" }}>
          Select Language
        </h3>

        <select
          value={language}
          onChange={(e) =>
            setLanguage(e.target.value)
          }
          style={{
            padding: "10px",
            borderRadius: "8px",
            fontSize: "16px"
          }}
        >
          <option>English</option>
          <option>Hindi</option>
          <option>Telugu</option>
          <option>Tamil</option>
          <option>Malayalam</option>
        </select>

        <br />
        <br />

        {!story && (

          <button
            style={{
              ...buttonStyle,
              background: "#28a745"
            }}
            onClick={generateStory}
          >
            📖 Generate Story
          </button>

        )}

        {storyLoading && (

          <h2
            style={{
              color: "#4CAF50",
              marginTop: "20px"
            }}
          >
            📖 Generating Story...
          </h2>

        )}

        

        {story && (

          <div style={cardStyle}>

            <h2
              style={{
                background: "black",
                color: "white",
                padding: "12px",
                borderRadius: "10px"
              }}
            >
              📖 Generated Story
            </h2>

            <pre
              style={{
                whiteSpace: "pre-wrap",
                color: "#000",
                fontSize: "16px",
                fontFamily: "inherit"
              }}
            >
              {story}
            </pre>

            {!script && (

              <button
                style={{
                  ...buttonStyle,
                  background:
                    "linear-gradient(135deg,#ff6a00,#ee0979)"
                }}
                onClick={generateTrailer}
              >
                🎬 Generate Visuals
              </button>

            )}
{trailerLoading && (

          <h2
            style={{
              color: "#FF9800",
              marginTop: "20px"
            }}
          >
            🎬 Creating Visuals...
          </h2>

        )}
          </div>

        )}

        {script && (

          <div style={cardStyle}>

            <h2
              style={{
                background: "black",
                color: "white",
                padding: "12px",
                borderRadius: "10px"
              }}
            >
              🎙 Trailer Narration
            </h2>

            <pre
              style={{
                whiteSpace: "pre-wrap",
                color: "#000",
                fontSize: "16px",
                fontFamily: "inherit"
              }}
            >
              {script}
            </pre>

          </div>

        )}

        {videoUrl && (

          <div style={cardStyle}>

            <h2
              style={{
                background: "black",
                color: "white",
                padding: "12px",
                borderRadius: "10px"
              }}
            >
              🎥 Generated Visuals
            </h2>

            <video
              controls
              width="100%"
              src={videoUrl}
              style={{
                borderRadius: "10px"
              }}
            >
              Your browser does not support video.
            </video>

          </div>

        )}

      </div>

    </div>

  );
}

export default App;