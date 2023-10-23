/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type UserRegistration = {
    email: string;
    password: string;
    firstName: string;
    lastName: string;
    /**
     * * `owner` - owner
     * * `broker` - broker
     * * `staff` - staff
     */
    role: 'specialist' | 'parent';
};

