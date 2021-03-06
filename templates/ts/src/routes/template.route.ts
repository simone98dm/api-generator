import express from "express";
import { prefix } from "../configs/REPLACEME.config";
const router = express.Router();
router.get(prefix, async (req, res) => {
  return res.status(200).json().end();
});
router.get(prefix + "/:id", async (req, res) => {
  if (!req.params.id) {
    return res.status(404).end();
  }
  return res.status(200).json().end();
});
router.post(prefix, async (req, res) => {
  if (!req.body) {
    return res.status(404).end();
  }
  return res.status(200).json().end();
});
router.put(prefix, async (req, res) => {});
router.delete(prefix, async (req, res) => {});
export { router };
