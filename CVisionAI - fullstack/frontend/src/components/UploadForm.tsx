import "../css/UploadForm.css";
import { useState } from "react";
import {postData} from "../services/api"
import type {AnalysisResponse} from "../types/analysis"


type UploadFormProps = {
    setResult: React.Dispatch<React.SetStateAction<AnalysisResponse | undefined>>;
};

function UploadForm({ setResult }: UploadFormProps) {

     const [cv,setCv] = useState<File | null>(null);
     const [areaText,setAreaText] = useState("")
     const [error,setError] = useState("")
     const [loading,setLoading] = useState(false)


const handleClick = async() => {

    if (!cv || !areaText) {
        setError("Both fields are required.");
        return;
    }
 setLoading(true)
    const form = new FormData();

    form.append("pdf_data", cv);
    form.append("job_description", areaText);

    const result = await postData(form);
    if (result) {
      setLoading(false)
    }
    setCv(null)
    setAreaText("")
    setResult(result);
};

  return (
    <div className="parent">
      <div className="form-card">
        <h3 style={{"color":"red"}}>{error}</h3>
        <label className="label">Job Description</label>
        <textarea
          className="textarea"
          placeholder="Paste the job description here..."
          value={areaText}
        onChange={(e) => setAreaText(e.target.value)}/>
       

        <div className="forFile">
          <label className="label">Upload Your CV</label>

          <label className="file-upload">  
            <input type="file" onChange={(e) => setCv(e.target.files?.[0] ?? null)}/>
          
            <span> {cv === null ? "📄 Choose your CV" : cv.name}</span>
        </label>
        </div>

        <button className="button" onClick={() => handleClick()}>
          {loading === false ? "Analyze CV" : "Loading..." } 
        </button>

            
      </div>






    </div>

  );
}

export default UploadForm;