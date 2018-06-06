var mongoose = require('mongoose');

var AutomationSchema = new mongoose.Schema({

    name: {
        type: String,
        required: true,
        unique: true
    }, active: {
        type: Number,
        default: 0
    },dt: {
        type: String,
        default: "08:00"
    },nt: {
        type: String,
        default: "22:00"
    },temp: {
        type: Number,
        default: 20
    },humidity: {
        type: Number,
        default: 45
    },vdr: {
        type: Number,
        default: 0
    },vnr: {
        type: Number,
        default: 0
    },bdr: {
        type: Number,
        default: 0
    },bnr: {
        type: Number,
        default: 0
    }
});


var Automation = mongoose.model('Automation', AutomationSchema);
module.exports = Automation;