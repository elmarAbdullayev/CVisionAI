import type {AnalysisResponse} from "../types/analysis"
import "../css/AnalysisResult.css"


type AnalysisResultProps = {
    result?: AnalysisResponse;
};

function AnalysisResult({ result }: AnalysisResultProps) {

   if (!result) {
        return <p>No result yet.</p>;
    }

 return (
  <div className="analysis-container">
    <div className="score-card">
      <h2>Match Score</h2>
      <div className="score">{result.match_score}%</div>
    </div>

    <div className="card">
      <h3>✅ Passende Skills</h3>
      <ul>
        {result.skills.map((skill) => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>
    </div>

    <div className="card">
      <h3>❌ Fehlende Skills</h3>
      <ul>
        {result.missing_skills.map((skill) => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>
    </div>

    <div className="card">
      <h3>💡 Verbesserungsvorschläge</h3>
      <ul>
        {result.improvements.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>

    <div className="card">
      <h3>📄 Anschreiben</h3>
      <p>{result.cover_letter}</p>
    </div>
  </div>
);
}

export default AnalysisResult;
