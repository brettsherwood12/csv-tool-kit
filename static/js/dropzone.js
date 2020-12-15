const generateFilename = () => {
  const dateTime = Date.now().toString();
  const filename = `userfile_${dateTime}.csv`;
  return filename;
};

const filename = generateFilename();

const myDropzone = new Dropzone("div#dropzone", {
  url: "/upload",
  thumbnailWidth: 120,
  thumbnailHeight: 120,
  sending: function (file, xhr, formData) {
    formData.append("filename", "blah");
  }
});
