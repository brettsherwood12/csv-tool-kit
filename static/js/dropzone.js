const form = document.getElementById("dropzone-form");

const action = form.action.split("/")[3];

const generateFilename = () => {
  const dateTime = Date.now().toString();
  const filename = `userfile_${dateTime}.csv`;
  return filename;
};

const myDropzone = new Dropzone("div#dropzone", {
  url: `/${action}`
});

myDropzone.on("sending", (file, xhr, formData) => {
  const filename = generateFilename();
  formData.append("filename", filename);
});
