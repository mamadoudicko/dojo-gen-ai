import React from "react"
import ReactDOM from "react-dom"
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib"
import { App } from "./App"

class AiNoteTaker extends  StreamlitComponentBase {
  render = () =>{
    return <App />
  }
}

const Main =  withStreamlitConnection(AiNoteTaker)

Streamlit.setComponentReady()

Streamlit.setFrameHeight()

ReactDOM.render(
  <React.StrictMode>
    <Main />
  </React.StrictMode>,
  document.getElementById("root")
)
