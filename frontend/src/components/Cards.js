import React, { useState, useRef } from 'react';
import './Cards.css';


function Cards() {
  const [image, setImage] = useState(null);
  const hiddenFileInput = useRef(null);
  const hiddenFileInput1 = useRef(null);

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    const imgname = event.target.files[0].name;
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = () => {
      const img = new Image();
      img.src = reader.result;
      img.onload = () => {
        const canvas = document.createElement("canvas");
        const maxSize = Math.max(img.width, img.height);
        canvas.width = maxSize;
        canvas.height = maxSize;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(
          img,
          (maxSize - img.width) / 2,
          (maxSize - img.height) / 2
        );
        canvas.toBlob(
          (blob) => {
            const file = new File([blob], imgname, {
              type: "image/jpg",
              lastModified: Date.now(),
            });

            console.log(file);
            setImage(file);
          },
          "image/jpeg",
          0.8
        );
      };
    };
  };

  const handleImageChange1 = (event) => {
    const file = event.target.files[0];
    const imgname = event.target.files[0].name;
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = () => {
      const img = new Image();
      img.src = reader.result;
      img.onload = () => {
        const canvas1 = document.createElement("canvas");
        const maxSize = Math.max(img.width, img.height);
        canvas1.width = maxSize;
        canvas1.height = maxSize;
        const ctx = canvas1.getContext("2d");
        ctx.drawImage(
          img,
          (maxSize - img.width) / 2,
          (maxSize - img.height) / 2
        );
        canvas1.toBlob(
          (blob) => {
            const file = new File([blob], imgname, {
              type: "image/jpg",
              lastModified: Date.now(),
            });

            console.log(file);
            setImage(file);
          },
          "image/jpeg",
          0.8
        );
      };
    };
  };


  const handleClick = (event) => {
    hiddenFileInput.current.click();
  };

  const handleClick1 = (event) => {
    hiddenFileInput1.current.click();
  };
  return (
    <div className='cards' id='cards'>

      <div className="image-upload-container">
        <div className="box-decoration">
          <ul className='cards__items'>
            <label htmlFor="image-upload-input-1" className="image-upload-label">
              {image ? "Before Change Image" : "Upload Before Change Image"}
            </label>
            <div onClick={handleClick} style={{ cursor: "pointer" }}>
              {image ? (
                <img src={URL.createObjectURL(image)} alt="upload image" className="img-display-after" />
              ) : (
                <img src="images/input.jpg" alt="upload image" className="img-display-before" />
              )}

              <input
                id="image-upload-input-1"
                type="file"
                onChange={handleImageChange}
                ref={hiddenFileInput}
                style={{ display: "none" }}
              />
            </div>
          </ul>
          <ul className='cards__items'>
            <label htmlFor="image-upload-input-2" className="image-upload-label">
              {image ? "After Change Image" : "Upload After Change Image"}
            </label>
            <div onClick={handleClick1} style={{ cursor: "pointer" }}>
              {image ? (
                <img src={URL.createObjectURL(image)} alt="upload image" className="img-display-after" />
              ) : (
                <img src="/images/input.jpg" alt="upload image" className="img-display-before" />
              )}

              <input
                id="image-upload-input-2"
                type="file"
                onChange={handleImageChange1}
                ref={hiddenFileInput1}
                style={{ display: "none" }}
              />
            </div>
          </ul>
          
        </div>
      
      </div>

    </div>
  );

}

export default Cards;