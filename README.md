## ✅ Pydantic Cheat Sheet Summary

| Feature              | Usage Example                                  |
| -------------------- | ---------------------------------------------- |
| Type Coercion        | `"30"` → `30`                                  |
| Email Validation     | `EmailStr`                                     |
| URL Validation       | `AnyUrl`                                       |
| Field Constraints    | `Field(gt=0, max_length=50)`                   |
| Optional Fields      | `Optional[str] = None`                         |
| Annotated Fields     | `Annotated[str, Field(...)]`                   |
| Nested Models        | Models inside Models                           |
| Custom Validators    | `@field_validator('field')`                    |
| Serialization (dict) | `model.model_dump()`                           |
| Serialization (JSON) | `model.model_dump_json()`                      |
| Validation Modes     | `mode='before'` or `mode='after'`              |
| Examples in Docs     | `Field(..., examples=['abc', 'xyz'])`          |
| Title & Description  | `Field(..., title="Title", description="...")` |
| Strict Types         | `Field(strict=True)`                           |
