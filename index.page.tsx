import React from "react";
import styled from "styled-components";
import tutorialsIcon from "./assets/site/icons/tutorials.svg";
import onboardingIcon from "./assets/site/icons/onboarding.svg";
import resourcesIcon from "./assets/site/icons/resources.svg";
import { ArrowRightIcon, Button } from "@redocly/theme";
import { Card } from "@redocly/theme/markdoc/components/Cards/Card";
import { Cards } from "@redocly/theme/markdoc/components/Cards/Cards";

const Container = styled.div`
    padding: 2rem;
`;

const Header = styled.div`
    text-align: center;
    margin-bottom: 3rem;
`;

const Title = styled.h1`
    font-size: 2.5rem;
    margin-bottom: 1rem;
`;

const Subtitle = styled.h2`
    font-size: 1.5rem;
    font-weight: normal;
    margin-bottom: 2rem;
`;

const CardSection = styled.section`
    display: flex;
    justify-content: space-around;
    padding: 3rem 0;
    text-decoration: none;
    color: inherit;
    cursor: pointer;
    transition: transform 0.2s;

    &:hover {
        transform: translateY(-2px);
    }
`;

const DlCard = styled.div`
    text-align: center;
    max-width: 300px;
`;

const CardIcon = styled.div`
    margin-bottom: 1rem;
    svg {
        width: 48px;
        height: 48px;
        color: #007bff;
    }
`;

const CardLink = styled.a`
    text-decoration: none;
    color: inherit;
    display: block;
`;

export default function HomePage() {
    return (
        <Container>
            <Header>
                <Title>Dataloop Developers Portal</Title>
                <Subtitle>
                    A developer portal for beginners and advanced users
                </Subtitle>
                <Button
                    variant="outlined"
                    size="xlarge"
                    to="/tutorials/getting_started/sdk_overview/chapter"
                >
                    Get started <ArrowRightIcon />
                </Button>
            </Header>
            <Cards>
                <CardLink href="/tutorials">
                    <CardSection>
                        <CardIcon>
                            <img src={tutorialsIcon} alt="Tutorials" />
                        </CardIcon>
                        <DlCard>
                            <h3>Tutorials</h3>
                            Step-by-step guides to get started with Dataloop
                        </DlCard>
                    </CardSection>
                </CardLink>
                <CardLink href="/onboarding/onboarding">
                    <CardSection>
                        <CardIcon>
                            <img src={onboardingIcon} alt="Onboarding" />
                        </CardIcon>
                        <DlCard>
                            <h3>Onboarding</h3>
                            Get up and running with Dataloop platform
                        </DlCard>
                    </CardSection>
                </CardLink>
                <CardLink href="/resources">
                    <CardSection>
                        <CardIcon>
                            <img src={resourcesIcon} alt="Resources" />
                        </CardIcon>
                        <DlCard>
                            <h3>Resources</h3>
                            SDKs, APIs and developer tools
                        </DlCard>
                    </CardSection>
                </CardLink>
            </Cards>
        </Container>
    );
}
