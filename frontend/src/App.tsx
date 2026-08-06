import UploadForm from "./components/UploadForm"
import AnalysisResult from "./components/AnalysisResult"
import type {AnalysisResponse} from "./types/analysis"
import { useState } from "react";

function App() {

const [result, setResult] = useState<AnalysisResponse | undefined>();

  return (
    <>
<UploadForm setResult={setResult}/>
<AnalysisResult result={result}/>
    </>
  )
}

export default App
