const express = require("express");
const config = require("../configs/REPLACEME.config");
const router = express.Router();
router.get(config.prefix, async (req, res) => {
  return res.status(200).json().end();
});
router.get(config.prefix + "/:id", async (req, res) => {
  if (!req.params.id) {
    return res.status(404).end();
  }
  return res.status(200).json().end();
});
router.post(config.prefix, async (req, res) => {
  if (!req.body) {
    return res.status(404).end();
  }
  return res.status(200).json().end();
});
router.put(config.prefix, async (req, res) => {});
router.delete(config.prefix, async (req, res) => {});
module.exports = router;
