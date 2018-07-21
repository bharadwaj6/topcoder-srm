import React from 'react';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
      dropdetails: [],
      best_droplet_index: null,
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
    this.pushUploadImage = this.pushUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);

    fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        console.log('called the method after response');
        this.setState({ imageURL: `http://localhost:8000/${body.file}` });
        this.setState({dropdetails: body});
        this.setState({best_droplet_index: this.setState.best_droplet_index})
      });
    });
  }
  
  pushUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('best_droplet_index', this.state.dropdetails.best_droplet_index);

    fetch('http://localhost:8000/push_upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        console.log('called the method after response');
        this.setState({ imageURL: `http://localhost:8000/${body.file}` });
        this.setState({dropdetails: body});
        this.setState({best_droplet_index: this.setState.best_droplet_index})
      });
    });
  }

  render() {
    
    return (
      [<form onSubmit={this.handleUploadImage} enctype="multipart/form-data">
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <br />
        <div>
          <button>Get Details</button>
        </div>
    {this.state.dropdetails ? <div><pre>{JSON.stringify(this.state.dropdetails, null, 2) }</pre></div> : <div> No details yet. Upload something.</div> }
      </form>,
      <form onSubmit={this.pushUploadImage} enctype="multipart/form-data"> <button>Confirm upload</button> <input type="hidden" name="best_droplet_index" id="best_droplet_index" value={this.state.dropdetails.best_droplet_index}/></form>
      ]
    );
  }
}

export default Main;
