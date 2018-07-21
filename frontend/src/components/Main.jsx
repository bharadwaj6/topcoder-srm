import React from 'react';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
      dropdetails: [],
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('filename', this.fileName.value);


    var myHeaders = new Headers({
      // 'Access-Control-Allow-Origin': 'http://127.0.0.1:8000',
      // 'mode': 'no-cors'
    });

    fetch('http://localhost:8000/upload', {
      method: 'POST',
      headers: myHeaders,
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        this.setState({ imageURL: `http://localhost:8000/${body.file}` });
        this.setState({dropdetails: body});
      });
    });
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage} enctype="multipart/form-data">
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <div>
          <input ref={(ref) => { this.fileName = ref; }} type="text" placeholder="Enter the desired name of file" />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>
        
        <div><pre>{JSON.stringify(this.state.dropdetails, null, 2) }</pre></div>
      </form>
    );
  }
}

export default Main;
