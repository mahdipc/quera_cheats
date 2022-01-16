import React, { useState } from "react";
import Select from "./Select";
import Input from "./Input";
import { units } from "../units";
const factor  = [
  {
    label: "Meter",
    value: "1000",
  },
  {
    label: "Centimeter",
    value: "100000",
  },
  {
    label: "Millimeter",
    value: "1000000",
  },
  {
    label: "Kilometer",
    value: "1",
  },
];

let Amount = React.createRef();
let To = React.createRef();
let From = React.createRef();

function App() {
  const [result, setResult] = useState(0);

  function handleClick() {
    const amount=Amount.current.value;
    const f=From.current.value;
    const t=To.current.value;
    
    // setResult(From.current.value);
    setResult(amount*t/f);

  }
  return (
    <>
      <div className="converter-form">
        <label>
    Amount:
    <input type="text" name="Amount" ref={Amount} />
  </label>
        <div className="row">
          <div>
          <label>
From:
        <select ref={From}>
            {factor.map((option) => (
              <option value={option.value}>{option.label}</option>
            ))}
          </select>
  </label>
          </div>
          <div>

          <label>
To:
        <select ref={To}>
            {factor.map((option) => (
              <option value={option.value}>{option.label}</option>
            ))}
          </select>
  </label>
          </div>

          <button  onClick={handleClick}>Convert</button>
        </div>
      </div>

      <div id="result">
        Result is: <span data-testid="result">{result}</span>
      </div>
    </>
  );
}

export default App;
