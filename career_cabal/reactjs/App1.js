import React from "react"
import { render } from "react-dom"

class App1 extends React.Component {
  render() {
    return (
     <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <h1>Hello React</h1>
          </div>
        </div>
      </div>
    )
  }
}

render(<App1/>, document.getElementById('App1'))