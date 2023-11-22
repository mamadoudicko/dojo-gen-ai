import AudioReactRecorder, { RecordState } from 'audio-react-recorder';
import 'audio-react-recorder/dist/index.css';
import React, { useState } from "react";
import { Streamlit } from "streamlit-component-lib";

export const App = () => {
  const [recordState, setRecordState] = useState(null);
  const [audioDataURL, setAudioDataURL] = useState('');

  const onClick = () => {
    if (recordState === RecordState.START) {
      setRecordState(RecordState.STOP);
      return 
    } 
    setAudioDataURL('');
    setRecordState(RecordState.START);
  };

  const onStop = (data) => {
    setAudioDataURL(data.url);
    data.blob.arrayBuffer().then((arrayBuffer) => {
       const uint8Array = new Uint8Array(arrayBuffer);
        Streamlit.setComponentValue({ "arr": uint8Array });
     });
  };
  
  const recordButtonLabel = recordState === RecordState.START ? 'Stop Recording' : 'Start Recording'

  return (
    <div>
      <button 
        id='toggle'
        onClick={onClick} 
        style={{
          marginBottom: 10
        }}
      >
        {recordButtonLabel}
      </button>
      
      <AudioReactRecorder
        state={recordState}
        onStop={onStop}
        canvasHeight={20}
      />

      <audio
        id='audio'
        controls
        src={audioDataURL}
        style={{
          marginTop: 10
        }}
      />
    </div>
  );
};
