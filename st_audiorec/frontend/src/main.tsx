
import React from "react"
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


export const Main =  withStreamlitConnection(AiNoteTaker)

Streamlit.setComponentReady()

Streamlit.setFrameHeight()