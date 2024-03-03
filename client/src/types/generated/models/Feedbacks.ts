interface FeedbackDetail {
  [key: string]: number;
}

interface Feedback {
  [role: string]: FeedbackDetail;
}

interface FeedbackEntry {
  id: string;
  date: string;
  feedback: Feedback;
}

export type Feedbacks = FeedbackEntry[];
