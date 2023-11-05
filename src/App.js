import './App.css';
import {useState} from 'react';
import Title from './Title';
import Button from './Button';
import Content from './Content';

let stage = 0;

function App() {

  //Application Constants
  const titleVals = ['Housing Eligibility Assistant', 'Data Input', 'Approved', 'Denied'];
  const buttonNameVals = ['Next', 'Submit', 'Return'];
  const contentVals = [
      (<div id="stage1">
          <p>
            A handy tool for estimating you financial eligibility for purchancing a house
          </p>
      </div>),
      (<div id="stage2">

      </div>),
      (<div id="stage3">

      </div>)];

  //Title of the page
  const [title, setTitle] = useState(titleVals[stage]);
 
  //Content of the page
  const [content, setContent] = useState((contentVals[stage]));

  //Name of the transition of the button
  const [buttonName, setButtonName] = useState(buttonNameVals[stage]);
  const callback = () => {

        stage++;
 
        if(stage > 2) {

          stage = 0;

        }

        setTitle(titleVals[stage]);
        setButtonName(buttonNameVals[stage]);
        setContent(contentVals[stage]);

  }

      

  return (
      <div className="app">
        <Title title={title} />
        <Content content={content} />
        <Button callback={callback} name={buttonName} />
      </div>
  );
}

export default App;
